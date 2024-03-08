from hydra import initialize, compose
# from omegaconf import DictConfig, OmegaConf
# from torch import multiprocessing
import os

import numpy as np
# import random
# from collections import defaultdict
# import time

import os
# import random
import time
# import traceback
import pandas as pd

import numpy as np
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
from tqdm import tqdm
# from functools import partial
# from copy import deepcopy
# from enum import Enum

from utils.logging_utils import create_logger_in_process, generate_log_file_path
from utils.exp_utils import seed_all, config_to_dict, dict_to_config
# from utils.results_utils import normalize_means, generate_main_results_table
import re
# from simulate import simulate
from rate_limiter import ChatRateLimiter

# import atexit
# import click
# import datetime
import os
# import requests
import sys
# import yaml
import json
import openai
# from functools import partial
# from openai.embeddings_utils import cosine_similarity

# from pathlib import Path
# from prompt_toolkit import PromptSession, HTML
# from prompt_toolkit.history import FileHistory
# from rich.console import Console
# from rich.markdown import Markdown

from llm_utils import setup_chat_rate_limiter, chat_completion_rl, get_llm_config, num_tokens_consumed_by_chat_request, get_model_max_tokens, embedding_rl, pretty_print_chat_messages
# # from summarizer_and_modifier import load_code_files_into_dict, count_total_characters, count_key_characters, extract_file_names, format_files_into_prompt_format, embed_all_code_files, cache_or_compute, remove_line_numbers
# from diff_merger import implement_git_diff_on_file_dict
# from executor import pytest_code_base, python_run_code_base
# from utils.checkpoint_utils import dump_locals_to_json
# from llm_utils import num_tokens_from_functions
# from openai.error import InvalidRequestError
# from summarizer_and_modifier import fix_line_spacings, fix_indentation
# from utils.indenter_utils import reindent_lines
from llm_utils import num_tokens_from_messages
import os
import sys
from pygount import SourceAnalysis
import subprocess
import sys
from radon.complexity import cc_visit
# from radon.raw import analyze
import subprocess
# import pickle
# import base64
# import traceback
# import ast
from pathlib import Path
from tempfile import TemporaryDirectory
from pathlib import Path
import tempfile
import os
from summarizer_and_modifier import write_files_from_dict
import json
# from timeout_decorator import timeout
from utils.plot_utils import plot_error_plots, plot_write_heatmaps
from diff_merger import implement_git_diff_on_file_dict
from summarizer_and_modifier import write_files_from_dict, check_syntax, check_pytest, count_errors_in_syntax, parse_and_print_junit_xml, load_code_files_into_dict

PROCESS_FEATURES = True

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
        return (0,0)
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
            return (0,0)

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

def pytest_code_base(file_dict, files_to_test=None):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        # write_files_from_dict(file_dict)
        command = ["pytest"]
        if files_to_test is not None:
            command.extend(files_to_test)
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True,
            cwd=tmpdirname)
    captured_output = result.stdout.strip()
    # print(captured_output)
    return captured_output



def count_errors_from_file_dict(file_dict):
    """
    Count the number of errors in a given Python code file using pylint.

    :param file_path: Path to the Python code file.
    :return: Number of errors.
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        errors = count_errors(tmpdirname)
    return errors

def run_tests_from_file_dict(file_dict):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        tests = run_tests_and_get_pass_percentage(tmpdirname)
    return tests

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
    match = re.search(r'FEATURES_DESCRIBED=(\d+)', text)
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

import json

def extract_json_responses(log_content):
    # Maintain a buffer to collect lines that form a JSON object
    json_buffer = []
    # Maintain a count to know how deep inside the JSON we are
    open_brace = 0
    # List to store extracted JSON objects
    json_objects = []
    
    for line in log_content:
        if 'DEBUG' in line and line.strip()[-1] in ['{', '[']:
            open_brace = 1
            json_buffer.append(line.strip()[-1])
        elif line and line[0] in ['}', ']']:
            open_brace = 0
            json_buffer.append(line.strip())
            if len(json_buffer) > 0:
                try:
                    json_obj = json.loads(' '.join(json_buffer))
                    json_objects.append(json_obj)
                except json.JSONDecodeError:
                    pass
                json_buffer.clear()
        elif open_brace == 1:
            json_buffer.append(line.strip())
    return json_objects

def load_auto_gpt_log_file(autogpt_path):
    # read all lines in file
    with open(autogpt_path, 'r') as f:
        lines = f.readlines()
    json_blobs = extract_json_responses(lines)
    return json_blobs

def check_pytest_return_full_count(file_dict: dict):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        command = ['python3', '-m',  'pytest', '--junitxml=result_pytest.xml']
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



def process_log_instructions():
    initialize(config_path="config", version_base=None)
    config = compose(config_name="config.yaml")
    log_path = generate_log_file_path(__file__, log_folder=config.setup.log_dir, config=config)
    logger = create_logger_in_process(log_path)
    max_tokens = get_model_max_tokens(config)
    request_limit, token_limit = setup_chat_rate_limiter(config)
    rate_limiter = ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)
    seed_all(0)

    env_id = 'whatsapp'
    # for method in ['autogpt', 'llmatic']:
    for method in ['autogpt']:
        if method == 'autogpt':
            autogpt_path = 'examples/replay_example/whatsapp_run.log'
            json_turns = load_auto_gpt_log_file(autogpt_path)

            goal_summary = json_turns[1]['choices'][0]['message']['content']
        elif method == 'llmatic':
            llmatic_json_path = 'results/latest/run-20230922-044053_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-twitter_0_10-runs_log/whatsapp/0/current_LLMatic_state.json'
            with open(llmatic_json_path, 'r') as f:
                llmatic_json = json.load(f)
            msgs = [msg['content'] for msg in llmatic_json['meta_messages']]
            msgs.append('\n'.join(llmatic_json['steps']))
            goal_summary = '\n'.join(msgs)
        print(goal_summary)
        with open(f'data/donnemartin-system-design-oop/object_oriented_design/{env_id}/description_count.txt', "r") as f:
            task_description = f.read()
        steps = re.findall(r'\d+\.', task_description)
        total_features = len(steps)
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
        messages = [{"role": "system", "content": f'''
    Objective: Based on the numbered features given, you are to evaluate the following message and return a numeric value for how many (a count) of those numbered features are explicitly described in the provided message. Give the numeric answer as "FEATURES_DESCRIBED=num_features_described" in the final line.

    Numbered Features Specified:```
    {task_description}
    ```

    Message to evaluate for the amount of features fully described:"""
    {goal_summary}
    """
    '''}]
        response = get_llm_response(messages, config, rate_limiter)
        # print()
        # print(f"{method}: LOC: {locs_total} _ Errors: {errors} | Average Cyclomatic Complexity: {average_complexities}")
        features = extract_features_functional(response['content'])
        print(f'Method: {method}: Functional Features: {features}/{total_features} : {(features / total_features) * 100 :.2f}')

def process_log_errors():
    initialize(config_path="config", version_base=None)
    config = compose(config_name="config.yaml")
    log_path = generate_log_file_path(__file__, log_folder=config.setup.log_dir, config=config)
    logger = create_logger_in_process(log_path)
    max_tokens = get_model_max_tokens(config)
    request_limit, token_limit = setup_chat_rate_limiter(config)
    rate_limiter = ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)
    seed_all(0)

    env_id = 'whatsapp'
    # a = pd.read_csv('autogpt_errors.csv')
    # b = pd.read_csv('llmatic_errors_old.csv')
    # c = pd.read_csv('gpt4_errors.csv')
    # result = pd.concat([a, b, c], ignore_index=True)
    # plot_error_plots(result)
    # return

    # for method in ['autogpt', 'llmatic', 'gpt4']:
    for method in ['llmatic']:
        if method == 'autogpt':
            errors_df_l = []
            file_dict = {}
            count_change_times = 0
            # autogpt_path = 'examples/replay_example/whatsapp_run.log'
            autogpt_path = 'examples/replay_example/auto_gpt_workspace_whatsapp_new_1/activity.log'
            json_turns = load_auto_gpt_log_file(autogpt_path)
            commands_called = []
            chain_ops = []
            for obj in tqdm(json_turns):
                if 'choices' in obj and 'message' in obj['choices'][0] and 'content' in obj['choices'][0]['message']:
                    try:
                        content = json.loads(obj['choices'][0]['message']['content'])
                    except json.JSONDecodeError:
                        continue
                    commands_called.append(content['command']['name'])
                    if 'write_to_file' in obj['choices'][0]['message']['content']:
                        command = content['command']
                        # commands_called.append(command)
                        chain_ops.append(('write_files', command['args']['filename']))
                        if command['name'] == 'write_to_file':
                            file_dict[command['args']['filename']] = command['args']['text']
                            # errors = count_errors_from_file_dict(file_dict)
                            # tests = run_tests_from_file_dict(file_dict)
                            # syntax_results = check_syntax(file_dict)
                            # syntax_error_count = count_errors_in_syntax(syntax_results)
                            # (passed, total) = check_pytest_return_full_count(file_dict)
                            # errors_df_l.append({'change_count': count_change_times, 'errors': syntax_error_count, 'method': method, 'tests_passed': passed, 'tests_total': total})
                            # count_change_times += 1
            print(count_change_times)
            print(file_dict)
            print('')
            print(list(set(commands_called)))
            lists_of_lists = [[o[1]] for o in chain_ops if o[0] == 'write_files']
            all_files = list(set([item for sublist in lists_of_lists for item in sublist]))
            indx_files_exist = np.zeros(len(all_files))
            # indx_files_read = np.zeros(len(all_files))
            indx_files_exist_arr = []
            indx_files_written_arr = []
            # indx_files_read_arr = []
            for o in chain_ops:
                if o[0] == 'write_files':
                    indx_files_written = np.zeros(len(all_files))
                    f = o[1]
                    indx_files_exist[all_files.index(f)] = 1
                    indx_files_written[all_files.index(f)] += 1
                    indx_files_exist_arr.append(indx_files_exist.copy())
                    indx_files_written_arr.append(indx_files_written.copy())
                    # indx_files_read_arr.append(indx_files_read.copy())
                    indx_files_read = np.zeros(len(all_files))
                elif o[0] == 'view_files':
                    for f in o[1]:
                        indx_files_read[all_files.index(f)] += 1

            data = {'autogpt': {'indx_files_exist': np.array(indx_files_exist_arr), 'indx_files_written': np.array(indx_files_written_arr)}}
            np.array(indx_files_exist_arr)
            np.array(indx_files_written_arr)
            # np.array(indx_files_read_arr)
            plot_write_heatmaps(data)

            # syntax_results = check_syntax(file_dict)
            # print(syntax_results)
            # syntax_error_count = count_errors_in_syntax(syntax_results)
            
            autogpt = pd.DataFrame(errors_df_l)
            autogpt = autogpt.iloc[::2]
            # print('')
            autogpt.to_csv('autogpt_errors.csv')
            # b = pd.read_csv('llmatic_errors.csv')
            # plot_error_plots(a,b)
        elif method == 'llmatic':
            # llmatic_path = 'results/run-20230923-215025_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp_0_10-runs_log/whatsapp/0/LLMatic'
            # responses = 'results/run-20230923-215025_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp_0_10-runs_log/whatsapp/0/LLMatic_llm_responses.json'
            # responses = 'results/run-20230924-033218_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-twitter_0_5-runs_log/whatsapp/0/LLMatic_llm_responses.json'
            responses = 'results/final/twitter/9/LLMatic_llm_responses.json'
            with open(responses, 'r') as f:
                responses = json.load(f)
            file_dict = {}
            errors_df_l = []
            count_change_times = 0
            commands_called = []
            chain_ops = []
            for obj in tqdm(responses):
                if 'choices' in obj and 'message' in obj['choices'][0] and 'content' in obj['choices'][0]['message']:
                    if 'function_call' in obj['choices'][0]['message']:
                        commands_called.append(obj['choices'][0]['message']['function_call']['name'])
                        if obj['choices'][0]['message']['function_call']['name'] == 'view_files':
                            files = json.loads(obj['choices'][0]['message']['function_call']['arguments'])['files']
                            chain_ops.append(('view_files', files))
                        if obj['choices'][0]['message']['function_call']['name'] == 'write_files':
                            try:
                                args = json.loads(obj['choices'][0]['message']['function_call']['arguments'])
                                fs = args['files_and_contents']
                                chain_ops.append(('write_files', [d['file_path'] for d in fs]))
                            except json.JSONDecodeError:
                                continue
                            
                    if 'function_call' in obj['choices'][0]['message'] and 'write_files' == obj['choices'][0]['message']['function_call']['name']:
                        try:
                            args = json.loads(obj['choices'][0]['message']['function_call']['arguments'])
                        except json.JSONDecodeError:
                            continue
                        new_file_dict = implement_git_diff_on_file_dict(file_dict_input=file_dict,              
                                                    change_files_and_contents_input=args['files_and_contents'])
                        file_dict = new_file_dict
                        # syntax_results = check_syntax(file_dict)
                        # syntax_error_count = count_errors_in_syntax(syntax_results)
                        # (passed, total) = check_pytest_return_full_count(file_dict)
                        # errors_df_l.append({'change_count': count_change_times, 'method': method, 'errors': syntax_error_count,'tests_passed': passed, 'tests_total': total})
                        # count_change_times += 1
                        # write_files = content['command']
                        # if command['name'] == 'write_to_file':
                        #     file_dict = command['args']['file_dict']
                        #     errors = count_errors_from_file_dict(file_dict)
                        #     tests = run_tests_from_file_dict(file_dict)
                        #     errors_df_l.append({'change_count': count_change_times, 'errors': errors, 'method': method, 'tests_passed': tests[0], 'tests_total': tests[1]})
                        #     count_change_times += 1
            lists_of_lists = [o[1] for o in chain_ops if o[0] == 'write_files']
            all_files = list(set([item for sublist in lists_of_lists for item in sublist]))
            indx_files_exist = np.zeros(len(all_files))
            indx_files_read = np.zeros(len(all_files))
            indx_files_exist_arr = []
            indx_files_written_arr = []
            indx_files_read_arr = []
            for o in chain_ops:
                if o[0] == 'write_files':
                    indx_files_written = np.zeros(len(all_files))
                    for f in o[1]:
                        indx_files_exist[all_files.index(f)] = 1
                        indx_files_written[all_files.index(f)] += 1
                    indx_files_exist_arr.append(indx_files_exist.copy())
                    indx_files_written_arr.append(indx_files_written.copy())
                    indx_files_read_arr.append(indx_files_read.copy())
                    indx_files_read = np.zeros(len(all_files))
                elif o[0] == 'view_files':
                    for f in o[1]:
                        indx_files_read[all_files.index(f)] += 1

            data = {'llmatic': {'indx_files_exist': np.array(indx_files_exist_arr), 'indx_files_written': np.array(indx_files_written_arr), 'indx_files_read': np.array(indx_files_read_arr)}}
            # np.array(indx_files_exist_arr)
            # np.array(indx_files_written_arr)
            # np.array(indx_files_read_arr)
            plot_write_heatmaps(data)
            
            print(count_change_times)
            print(list(set(commands_called)))
            llmatic = pd.DataFrame(errors_df_l)
            llmatic.to_csv('llmatic_errors.csv')
            print('')
        elif method == 'gpt4':
            errors_df_l = []
            count_change_times = 0
            path = 'results/whatsapp_gpt4/ZeroShot'
            file_dict = load_code_files_into_dict(path)
            syntax_results = check_syntax(file_dict)
            syntax_error_count = count_errors_in_syntax(syntax_results)
            (passed, total) = check_pytest_return_full_count(file_dict)
            errors_df_l.append({'change_count': count_change_times, 'method': method, 'errors': syntax_error_count,'tests_passed': passed, 'tests_total': total})
            gpt4 = pd.DataFrame(errors_df_l)
            gpt4.to_csv('gpt4_errors.csv')
            print('')



        # print(f'Method: {method}: Functional Features: {features}/{total_features} : {(features / total_features) * 100 :.2f}')

if __name__ == "__main__":
    process_log_errors()
