import multiprocessing
import logging
from omegaconf import DictConfig

def generate_log_file_path(file, log_folder='logs', config = {}):
    import os, time, logging
    file_name = os.path.basename(os.path.realpath(file)).split('.py')[0]
    from pathlib import Path
    Path(f"./{log_folder}").mkdir(parents=True, exist_ok=True)
    path_run_name = '{}-{}'.format(file_name, time.strftime("%Y%m%d-%H%M%S"))
    return f"{log_folder}/{path_run_name}_{'-'.join(config.setup.methods_to_evaluate)}_{'-'.join(config.setup.envs_to_evaluate)}_{config.setup.seed_start}_{config.setup.seed_runs}-runs_log.txt"

def create_logger_in_process(log_file_path):
    logger = multiprocessing.get_logger()
    if not logger.hasHandlers():
        formatter = logging.Formatter("%(processName)s| %(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s")
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(log_file_path)
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    return logger