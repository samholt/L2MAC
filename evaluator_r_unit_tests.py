import unittest
import hydra
from hydra import initialize, compose
from omegaconf import DictConfig, OmegaConf
from torch import multiprocessing
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
import random

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
import re
from simulate import simulate
from rate_limiter import ChatRateLimiter

import atexit
import click
import datetime
import os
import requests
import sys
import yaml
import json
import openai
from functools import partial
from openai.embeddings_utils import cosine_similarity

from pathlib import Path
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.history import FileHistory
from rich.console import Console
from rich.markdown import Markdown

from llm_utils import setup_chat_rate_limiter, chat_completion_rl, get_llm_config, num_tokens_consumed_by_chat_request, get_model_max_tokens, embedding_rl, pretty_print_chat_messages
from summarizer_and_modifier import load_code_files_into_dict, count_total_characters, count_key_characters, extract_file_names, format_files_into_prompt_format, embed_all_code_files, cache_or_compute, remove_line_numbers
from diff_merger import implement_git_diff_on_file_dict
from executor import pytest_code_base, python_run_code_base
from utils.checkpoint_utils import dump_locals_to_json
from llm_utils import num_tokens_from_functions
from openai.error import InvalidRequestError
from summarizer_and_modifier import fix_line_spacings, fix_indentation
from utils.indenter_utils import reindent_lines
from llm_utils import num_tokens_from_messages
import os
import sys
from pygount import SourceAnalysis
import subprocess
import sys
from radon.complexity import cc_visit
from radon.raw import analyze
import subprocess
from summarizer_and_modifier import write_files_from_dict, check_syntax, check_pytest, count_errors_in_syntax, parse_and_print_junit_xml, load_code_files_into_dict
from tempfile import TemporaryDirectory
from pathlib import Path
import tempfile
from hydra.core.global_hydra import GlobalHydra
from utils.llm_tools import pytest_files
from executor import pytest_code_base_with_xml

PROCESS_FEATURES = True
CC_COMPLEXITY = False
MULTI_PROCESS = True
MODEL_IDS = ['gpt-4-0', 'gpt-4-1', 'gpt-4-2', 'gpt-4-3']

def check_pytest_return_full_count(file_dict: dict, files_to_test=None):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        command = ['python3', '-m',  'pytest', '--junitxml=result_pytest.xml']
        if files_to_test is not None:
            command.extend(files_to_test)
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True,
            cwd=tmpdirname)
        stderr = result.stderr
        stdout = result.stdout
        try:
            results = parse_and_print_junit_xml(Path(tmpdirname) / 'result_pytest.xml')
            total_tests = np.sum([r['total'] for r in results])
            total_passed = np.sum([r['passed'] for r in results])
        except FileNotFoundError as e:
            return (0,0)
        # print(stdout)
        # print(stderr)
        # print(results)
        # print('=====================')
    return (total_passed, total_tests)

def check_coverage_return_full_percent(file_dict: dict):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        command = ["coverage", "run", "-m", "pytest"]
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True,
            cwd=tmpdirname)
        stderr = result.stderr
        stdout = result.stdout
        command = ["coverage", "report"]
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True,
            cwd=tmpdirname)
        stderr = result.stderr
        match = re.search(r'TOTAL.*\s+(\d+%)', result.stdout)
        if match:
            # Convert percentage string to float
            cov = float(match.group(1).rstrip('%'))
        else:
            cov = 0.0
    return cov

def run_tests_and_get_pass_percentage(folder_path):
    """
    Run pytest on a given folder and return the percentage of tests that pass.

    :param folder_path: Path to the folder containing Python test files.
    :return: Percentage of tests that pass.
    """
    # Search for possible test files
    test_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith("test") and file.endswith(".py"):
                test_files.append(os.path.join(root, file))
    # print(test_files)

    if len(test_files) == 0:
        return 'NA'
    else:
        passed = 0
        failed = 0
        for test_path in test_files:
            # Run pytest and capture the output
            result = subprocess.run(["pytest", test_path], capture_output=True, text=True)
            
            # Extract summary from the pytest output
            summary = result.stdout.split("\n")[-2]  # The summary is typically the second last line
            
            # # If pytest found no tests, return 0% pass rate
            # if "no tests ran" in summary:
            #     return 'NA'
            
            # Extract the number of passed and failed tests
            if ('passed' in summary) and ('failed' in summary):
                failed += int(summary.split()[1]) if "failed" in summary else 0
                passed += int(summary.split()[3]) if "passed" in summary else 0
            elif ('failed' in summary):
                failed += int(summary.split()[1]) if "failed" in summary else 0
            elif ('passed' in summary):
                passed += int(summary.split()[1]) if "passed" in summary else 0

        total_tests = passed + failed
        if total_tests == 0:
            return 'NA'

        # Calculate the pass percentage
        # pass_percentage = (passed / total_tests) * 100
        
        return (passed, total_tests)


def calculate_cc_with_radon(file_path):
    """
    Calculates the cyclomatic complexity of a given file using radon.
    
    :param file_path: Path to the file.
    :return: A dictionary with function/method names as keys and their cyclomatic complexity as values.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()

        # Analyze the file content using radon's cc_visit function
        blocks = cc_visit(content)

        # Create a dictionary to store the results
        results = {}
        complexities = []
        for block in blocks:
            # The name of the function/method is block.name and its cyclomatic complexity is block.complexity
            results[block.name] = block.complexity
            complexities.append(block.complexity)
        if len(complexities) == 0:
            return None
        else:
            average_complexities = np.mean(np.nan_to_num(complexities))

            return average_complexities

    except Exception as e:
        print(f"An error occurred: {e}")
        # sys.exit(1)
        return 0


def count_errors(folder):
    """
    Count the number of errors in a given Python code file using pylint.

    :param file_path: Path to the Python code file.
    :return: Number of errors.
    """
    folder = f'{folder}/*.py'
    cmd = ['pylint', folder, '--enable=E', '--reports=n']

    # Run pylint using subprocess
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    # Split the output by lines and count the lines starting with 'E' (for Error)
    report = result.stdout
    pattern = r".+:\d+:\d+: [E]\d+: .+"
    errors = re.findall(pattern, report)
    # errors = [line for line in result.stdout.split('\n') if ': E' in line]
    # print(errors)

    return len(errors)


def count_lines_of_code(file_or_dir_path):
    """
    Count the number of lines of code in a given file or directory using pygount.

    :param file_or_dir_path: Path to the file or directory.
    :return: Number of source code lines.
    """
    try:
        # Analyze the given path
        analysis = SourceAnalysis.from_file(file_or_dir_path, "utf-8")

        # Return the number of code lines
        return analysis.code

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def get_paths(base_path="results"):
    """
    Generate paths based on the given folder structure: results/{env_name}/{seed}/{method}/
    """
    envs = os.listdir(base_path)
    paths = []

    for env in envs:
        env_path = os.path.join(base_path, env)
        
        if not os.path.isdir(env_path):
            continue  # skip files

        for seed in os.listdir(env_path):
            seed_path = os.path.join(env_path, seed)

            if not os.path.isdir(seed_path):
                continue  # skip files

            for method in os.listdir(seed_path):
                method_path = os.path.join(seed_path, method)

                if not os.path.isdir(method_path):
                    continue  # skip files

                paths.append(method_path)

    paths = [path for path in paths if 'run' not in path]
    return paths

# def get_paths_final(base_path="results"):
#     """
#     Generate paths based on the given folder structure: results/{env_name}/{seed}/{method}/
#     """
#     from pathlib import Path
#     result = list(Path(".").rglob("*.[tT][xX][tT]"))
#     return paths

def count_tokens_from_files(file_dict):
    file_dict_str = '\n'.join(['\n'.join(lines) for lines in file_dict.values()])
    tokens = num_tokens_from_messages([{"content": file_dict_str}])
    return tokens

def extract_features_functional(text):
    """
    Extract the number from a pattern 'FEATURES_FUNCTIONAL='.

    :param text: Input text to be parsed.
    :return: Extracted number as an integer or None if the pattern is not found.
    """
    match = re.search(r'FEATURES_FUNCTIONAL=(\d+)', text)
    return int(match.group(1)) if match else None


def get_llm_response(messages, config, rate_limiter):
    # num_tokens = num_tokens_consumed_by_chat_request(messages=messages)
    logger = None
    name = "TestSystemDesignPromptChains"
    llm_config = get_llm_config(config, logger, name, rate_limiter)
    llm_config['messages'] = messages
    llm_config['temperature'] = 0
    llm_config['top_p'] = 1.0
    try:
        response = chat_completion_rl(**llm_config)
    except openai.error.InvalidRequestError as e:
        print("Error:", e.__dict__)  # or use a logging framework
        raise
    message_response = response["choices"][0]["message"]
    if not message_response.get('content'):
        message_response['content'] = None
    return message_response

def get_cc_complexities(path):
    average_complexities = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split('.')[-1] == 'py':
                full_file_path = os.path.join(root, file)
                cc = calculate_cc_with_radon(full_file_path)
                if cc is not None:
                    average_complexities.append(cc)
                # locs += count_lines_of_code(full_file_path)

    average_complexities = np.mean(average_complexities)
    return average_complexities

def count_errors_in_syntax_and_fatal(syntax_output: str):
    pattern = r".+:\d+:\d+: [EF]\d+: .+"
    errors = re.findall(pattern, syntax_output)
    return len(errors)

def extract_content_v2(string):
    # Adjusting the regular expression pattern to correctly extract the content
    # The pattern looks for an optional '```python' followed by any content (including newlines),
    # followed by an optional '```', and captures the content in between
    pattern = r"```python(.*?)```|```(.*?)```|(.*?)"
    matches = re.findall(pattern, string, re.DOTALL)

    # Extract the non-empty match
    for match in matches:
        content = next((x for x in match if x), '').strip()
        if content:
            return content

    return ""  # Return empty string if no content is found


def process_path(args_for_run):
    model_id, path, seed = args_for_run
    # paths = get_paths(base_path='results/final_count')
    # paths = [p for p in paths if 'gpt4' not in p]
    if GlobalHydra.instance().is_initialized():
        GlobalHydra.instance().clear()
    initialize(config_path="config", version_base=None)
    config = compose(config_name="config.yaml")
    config.run.model = model_id
    log_path = generate_log_file_path(__file__, log_folder=config.setup.log_dir, config=config)
    logger = create_logger_in_process(log_path)
    max_tokens = get_model_max_tokens(config)
    request_limit, token_limit = setup_chat_rate_limiter(config)
    rate_limiter = ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)
    seed_all(0)
    # paths = [path for path in paths if ('llmatic' in path) and ('url' in path)]
    # paths = [path for path in paths if ('llmatic' in path.lower()) and ('url' in path)]
    # paths = [path for path in paths if not 'autogpt' in path]

    # p = 'results/run-20230923-215025_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp_0_10-runs_log/whatsapp/0/LLMatic'
    # # p = 'results/run-20230923-201355_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp_0_10-runs_log/whatsapp/0/LLMatic'
    # paths_0 = ['results/to_process/run-20230925-221829_LLMatic_donnemartin-system-design-oop-whatsapp_0_5-runs_log/whatsapp/1/LLMatic',
    #          'results/to_process/run-20230925-221829_LLMatic_donnemartin-system-design-oop-whatsapp_0_5-runs_log/whatsapp/0/LLMatic',
    #          'results/to_process/run-20230925-213616_LLMatic_donnemartin-system-design-oop-whatsapp_0_5-runs_log/whatsapp/0/LLMatic',
    #          'results/to_process/run-20230925-211447_LLMatic_donnemartin-system-design-oop-whatsapp_0_5-runs_log/whatsapp/0/LLMatic']
    # paths_1 = ['results/to_process/run-20230926-000812_LLMatic_donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-whatsapp_0_5-runs_log/dropbox/0/LLMatic',
    #          'results/to_process/run-20230926-000812_LLMatic_donnemartin-system-design-oop-twitter-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-whatsapp_0_5-runs_log/twitter/0/LLMatic']
    # paths = [p]
    # paths = paths_0
    # paths.extend(paths_1)
    # print('')

    try:
        env_id = path.split('/')[-3]
        # env_id = 'whatsapp'
        # seed = path.split('/')[-2]
        method = path.split('/')[-1].lower()
        # if method != 'llmatic':
        #     continue
        # if env_id != 'url_shortener':
        #     continue
        file_dict = load_code_files_into_dict(path, number_lines=False)

        syntax_results = check_syntax(file_dict)
        syntax_error_count = count_errors_in_syntax_and_fatal(syntax_results)
        (tests_passed, tests_total) = check_pytest_return_full_count(file_dict)
        if CC_COMPLEXITY:
            avg_cc = get_cc_complexities(path)

        # Get code coverage
        coverage_percent = check_coverage_return_full_percent(file_dict)


        locs_total = np.sum([len(lines) for lines in file_dict.values()])
        if not PROCESS_FEATURES:
            features = None
            total_features = 1
        else:
                
            files_prompt, files_missed_out = format_files_into_prompt_format(file_dict, character_limit=float('inf'))
            if len(files_missed_out) >= 1:
                logger.error(f'{method} {env_id} {seed} Files missed out: {files_missed_out}!!!')
                print('==========\n\n')
            # print(files_prompt)
            with open(f'data/donnemartin-system-design-oop/object_oriented_design/{env_id}/description_count.txt', "r") as f:
                task_description = f.read()
            with open(f'data/donnemartin-system-design-oop/object_oriented_design/{env_id}/unit_tests_train.py', "r") as f:
                unit_tests = f.read()
            # steps = re.findall(r'\d+\.', task_description)
            if env_id == 'whatsapp':
                total_features = 20
            elif env_id == 'url_shortener':
                total_features = 17
            elif env_id == 'twitter':
                total_features = 21
            elif env_id == 'dropbox':
                total_features = 24
            elif env_id == 'recipe':
                total_features = 20
            elif env_id == 'bookclub':
                total_features = 25
            elif env_id == 'eventplanner':
                total_features = 28
            elif env_id == 'finance':
                total_features = 29

            # total_features = len(steps)
            # print(task_description)

            # messages = [{"role": "system", "content": f'''
# Objective: You are to evaluate the following code and return a numeric value of how many usable and working features are implemented in the code. Think step-by-step, and only count features that are fully functional, and compare only with the features given in the following. For example, if a feature is partially implemented, but not fully functional, do not count it. Give the numeric answer as "FEATURES_FUNCTIONAL=num_features_functional" in the final line.
                    

# Task Description with features:```
# {task_description}
# ```

# Code to evaluate:"""
# {files_prompt}
# """
# '''}]
            format_rps = f'''
Objective: Adapt the given unit tests to test the given code implementation. Make sure the test implementation matches that in the given code, e.g. match the defined classes and methods to call and assert on the expected output for a passing test.

Existing fixed code implementation to use:```
{files_prompt}
```

Unit tests to adapt to code:```
{unit_tests}
```

Now return only in full all the unit tests in a python file.
'''
            # logger.info('=========PRE RSPONSE----------')
            # logger.info(format_rps)
            messages = [{"role": "system", "content": format_rps}]
            if False:
                print(messages[0]['content'])
            response = get_llm_response(messages, config, rate_limiter)
            adapted_unit_tests = response['content']
            adapted_unit_tests = extract_content_v2(adapted_unit_tests)
            file_dict['test_unit_tests_evaluate.py'] = adapted_unit_tests.split('\n')
            # test_results = pytest_code_base_with_xml(file_dict, ['test_unit_tests_evaluate.py'])
            (unit_tests_passed, unit_tests_total) = check_pytest_return_full_count(file_dict, ['test_unit_tests_evaluate.py'])
            messages = [{"role": "system", "content": f'''
Objective: Based on the numbered features given, you are to evaluate the following code and return a numeric value for how many (a count) of those numbered features are implemented in the provided code. Give the numeric answer as "FEATURES_FUNCTIONAL=num_features_functional" in the final line.

Numbered Features Specified:```
{task_description}
```

Code to evaluate for the amount of features fully implemented:"""
{files_prompt}
"""
'''}]


            response = get_llm_response(messages, config, rate_limiter)
            features = extract_features_functional(response['content'])

            # logger.info('=========MID----------')
            # logger.info(response['content'])
            # print(response['content'])
            # print('==========\n\n')

            # print()
            # print(f"{method}: LOC: {locs_total} _ Errors: {errors} | Average Cyclomatic Complexity: {average_complexities}")
            # features = extract_features_functional(response['content'])
        if features is None:
            features = 0
        # print('==========\n\n')
        # print(f"{method}: {response['content']}")
        # print(f"{method}: Functional Features: {features} | LOC: {locs_total} | Errors: {errors} | Average Cyclomatic Complexity: {average_complexities}")
        print(f'Method: {method}: Functional Features: {features}/{total_features} : {(features / total_features) * 100 :.2f} | Tests: {tests_passed}/{tests_total} | LOC: {locs_total} | Errors: {syntax_error_count}')
        result_dict = {'method': method.lower(),
                        'seed': seed,
                        'features': features,
                        'total_features': total_features,
                        'features_percent': (features / total_features) * 100,
                        'test_passed': tests_passed,
                        'test_total': tests_total,
                        'unit_test_passed': unit_tests_passed,
                        'unit_test_total': unit_tests_total,
                        'coverage_percent': coverage_percent,
                        'locs': locs_total,
                        'errors': syntax_error_count,
                        'path': path,
                        'env_name': env_id}
        return result_dict
        # logger.info(f'[Exp evaluation complete] {result_dict}')
        # [Exp evaluation complete] 
        # print('==========\n\n')
    except Exception as e:
        print(f'Error: {e}')
        logger.info(traceback.format_exc())
        print('==========\n\n')
        return {'Error': traceback.format_exc()}
        # continue


    # for root, dirs, files in os.walk(path):
    #     for file in files:
    #         file_path = os.path.join(root, file)
    #         # Your code to evaluate the generated code for each method goes here
    #         # For now, let's just print the file path
    #         print(file_path)


def process_files():
    # paths = get_paths(base_path='results/final')
    # from pathlib import Path
    # paths = list(Path("./results/final_count/"))
    import os
    from glob import glob


    # Clear the GlobalHydra instance if it's already initialized
    if GlobalHydra.instance().is_initialized():
        GlobalHydra.instance().clear()

    initialize(config_path="config", version_base=None)
    config = compose(config_name="config.yaml")
    log_path = generate_log_file_path(__file__, log_folder=config.setup.log_dir, config=config)
    logger = create_logger_in_process(log_path)

    # Main results table before rebuttal
    # PATH = "./results/final_count/"
    # Rebuttal table now
    # PATH = "./results/rebuttal/"
    PATH = "./results/rebuttal_apriori_unit_tests/"

    # python3 -m pylint --disable=all --enable=E --score=no CodeGenGPT CodeGenGPT/*.py main.py analytics.py url_shortener.py

    # PATH = "./results/final_count/autoextend/url_shortener/1/autogpt"
    low_paths = [x[0] for x in list(os.walk(PATH))]
    paths = []
    datasets = []
    for p in low_paths:
        m = p.split('/')[-1]
        if m.lower() in ['llmatic', 'autogpt', 'zeroshot', 'selfrefine', 'reflexion', 'codet']:
            dataset = p.split('/')[-3]
            datasets.append(f'{dataset}-{m}')
            paths.append(p)
    
    from collections import Counter
    cc = Counter(datasets)
    print(cc)

    if MULTI_PROCESS:
        pool_outer = multiprocessing.Pool(4)
    args_for_runs = tasks = [(MODEL_IDS[i % len(MODEL_IDS)], path, random.randint(0,1000)) for i, path in enumerate(paths)]
    t0 = time.perf_counter()
    if not MULTI_PROCESS:
        for args_for_run in tqdm(args_for_runs):
            result = process_path(args_for_run)
            logger.info(f'[Exp evaluation complete] {result}')
    else:
        for i, result in tqdm(enumerate(pool_outer.imap_unordered(process_path, args_for_runs)), total=len(args_for_runs), smoothing=0):
            logger.info(f'[Exp evaluation complete] {result}')
    time_taken = time.perf_counter() - t0
    logger.info(f'Time taken for all runs: {time_taken}s\t| {time_taken/60.0} minutes')
    if config.setup.multi_process_results:
        pool_outer.close()
    logger.info(f'[Complete] Shutting down.')

    


# # Assuming chatcompletion is a predefined function
# def chatcompletion(model_id, prompt):
#     # Simulate a task with the given model_id and prompt
#     print(f"Processing with {model_id}: {prompt}")
#     # ... (task implementation here)

# def process_task(args):
#     # Unpack arguments and call chatcompletion
#     model_id, prompt = args
#     chatcompletion(model_id, prompt)

# if __name__ == "__main__":
#     model_ids = ['GPT4-0', 'GPT4-1', 'GPT4-2', 'GPT4-3']
#     prompts = ["prompt1", "prompt2", "prompt3", ...]  # List of 160 prompts

#     # Pair each prompt with a model_id in a round-robin fashion
#     tasks = [(model_ids[i % len(model_ids)], prompt) for i, prompt in enumerate(prompts)]

#     # Create a pool of workers
#     with multiprocessing.Pool(len(model_ids)) as pool:
#         # Map the process_task function to each task
#         pool.map(process_task, tasks)




if __name__ == "__main__":
    process_files()
