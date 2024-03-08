import hydra
from omegaconf import DictConfig, OmegaConf
# from torch import multiprocessing
import os

import numpy as np
import random
from collections import defaultdict
import time

import os
import random
import time
import traceback
import pandas as pd

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from tqdm import tqdm
from functools import partial
from copy import deepcopy
from enum import Enum

from utils.logging_utils import create_logger_in_process, generate_log_file_path
from utils.exp_utils import seed_all, config_to_dict, dict_to_config
from utils.results_utils import normalize_means, generate_main_results_table

from llm_utils import setup_chat_rate_limiter

from simulate import simulate
from rate_limiter import ChatRateLimiter

class Experiment(Enum):
    MAIN_TABLE = 1


@hydra.main(version_base=None, config_path="config", config_name="config.yaml")
def run(config: DictConfig) -> None:
    log_path = generate_log_file_path(__file__, log_folder=config.setup.log_dir, config=config)
    logger = create_logger_in_process(log_path)
    request_limit, token_limit = setup_chat_rate_limiter(config)
    rate_limiter = ChatRateLimiter(request_limit=request_limit, token_limit=token_limit) # ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)
    config.run.log_path = log_path
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") if config.setup.cuda else "cpu"
    config.run.device = str(device)
    if config.setup.debug_mode:
        config.setup.multi_process_results = False    
    if config.setup.multi_process_results:
        multiprocessing.set_start_method('spawn')
        config.setup.wandb.track = False
    if config.setup.wandb.track:
        import wandb
        wandb.init(
            project=config.setup.wandb.project,
            config=config_to_dict,
        )
    else:
        wandb = None
    seed_all(0)
    logger.info(f'Starting run \t | See log at : {log_path}')
    if config.setup.flush_mode:
        logger.info(f'[WARNING] In FLUSH MODE -- TEST RUN ONLY')
        config.run.episodes = 1
        config.setup.seed_start = 0
        config.setup.seed_runs = 1
    logger.info(f'[Main Config] {config}')
    main(config, wandb, logger, rate_limiter)
    if config.setup.wandb.track:
        wandb.finish()
    logger.info('Run over. Fin.')
    logger.info(f'[Log found at] {log_path}')


def main(config, wandb, logger, rate_limiter):
    if config.setup.multi_process_results:
        pool_outer = multiprocessing.Pool(config.setup.multi_process_cores)
    args_for_runs = []
    t0 = time.perf_counter()
    experiment = Experiment[config.setup.experiment]
    if experiment == Experiment.MAIN_TABLE:
        for seed in range(config.setup.seed_start, config.setup.seed_runs + config.setup.seed_start):
            for env_name in config.setup.envs_to_evaluate:
                for method_name in config.setup.methods_to_evaluate:
                    args_for_runs.append((env_name, method_name, seed))
    evaluate_policy_single = partial(run_exp_wrapper_outer, config=config, wandb=wandb, rate_limiter=rate_limiter)
    results = []
    if not config.setup.multi_process_results:
        for args_for_run in args_for_runs:
                result = evaluate_policy_single(args_for_run)
                printable_result = {k : v.tolist() if isinstance(v, np.ndarray) else v for k,v in result.items()}
                logger.info(f'[Exp evaluation complete] {printable_result}')
                results.append(result)
    else:
        for i, result in tqdm(enumerate(pool_outer.imap_unordered(evaluate_policy_single, args_for_runs)), total=len(args_for_runs), smoothing=0):
                printable_result = {k : v.tolist() if isinstance(v, np.ndarray) else v for k,v in result.items()}
                logger.info(f'[Exp evaluation complete] {printable_result}')
                results.append(result)
    time_taken = time.perf_counter() - t0
    logger.info(f'Time taken for all runs: {time_taken}s\t| {time_taken/60.0} minutes')
    if config.setup.multi_process_results:
        pool_outer.close()
    df_results = pd.DataFrame(results)
    tables = generate_main_results_table(df_results)
    logger.info(f'Tables: {tables}')
    print('')
    # print(table_str)
    print('fin.')

def run_exp_wrapper(args, logger, **kwargs):
    (env_name, method_name, seed) = args
    seed_all(seed)
    config = kwargs['config']
    config = dict_to_config(deepcopy(OmegaConf.to_container(config, resolve=True)))
    kwargs['config'] = config
    result = run_exp(env_name=env_name,
                        method_name=method_name,
                        seed=seed,
                        logger=logger,
                        **kwargs)
    result['errored'] = False
    return result

def run_exp_wrapper_outer(args, **kwargs):
    (env_name, method_name, seed) = args
    config = kwargs['config']
    logger = create_logger_in_process(config.run.log_path)
    logger.info(f'[Now evaluating exp] {args}')
    if config.setup.debug_mode:
        result = run_exp_wrapper(args, logger, **kwargs)
    else:
        try:
            result = run_exp_wrapper(args, logger, **kwargs)
        except Exception as e:
            logger.exception(f'[Error] {e}')
            logger.info(f"[Failed evaluating exp] {args}\t| error={e}")
            traceback.print_exc()
            result = {'errored': True}
            print('')            
    result.update({'env_name': env_name, 'seed': seed, 'method_name': method_name})
    return result

def run_exp(env_name,
            method_name,
            seed,
            logger,
            rate_limiter,
            config={},
            wandb=None):
    logger.info(f'Running {env_name} {method_name} {seed}')
    t00 = time.perf_counter()
    result = simulate(env_name,
            method_name,
            seed,
            logger,
            rate_limiter,
            config,
            wandb)
    seconds_taken = time.perf_counter() - t00
    result.update({'method': method_name, 'seed': seed, 'seconds_taken': seconds_taken})
    return result

if __name__ == "__main__":
    run()
