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

from pathlib import Path
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.history import FileHistory
from rich.console import Console
from rich.markdown import Markdown

from llm_utils import setup_chat_rate_limiter, chat_completion_rl, get_llm_config, num_tokens_consumed_by_chat_request, get_model_max_tokens
from summarizer_and_modifier import load_code_files_into_dict, count_total_characters, count_key_characters, extract_file_names, format_files_into_prompt_format

class TestSystemDesignPromptChains(unittest.TestCase):


    def get_llm_response(self):
        num_tokens = num_tokens_consumed_by_chat_request(messages=self.messages)
        logger = None
        name = "TestSystemDesignPromptChains"
        llm_config = get_llm_config(self.config, logger, name, self.rate_limiter)
        llm_config['messages'] = self.messages
        llm_config['temperature'] = 1.0
        llm_config['top_p'] = 1.0
        llm_config['functions'] = self.functions
        try:
            response = chat_completion_rl(**llm_config)
        except openai.error.InvalidRequestError as e:
            print("Error:", e.__dict__)  # or use a logging framework
            raise
        message_response = response["choices"][0]["message"]
        if not message_response.get('content'):
            message_response['content'] = None
        self.messages.append(message_response)
        return message_response


    def setUp(self):
        # This is run once before any tests or test methods in the class.
        # Initialize Hydra
        initialize(config_path="config", version_base=None)  # Point to your actual config directory
        self.config = compose(config_name="config.yaml")
        request_limit, token_limit = setup_chat_rate_limiter(self.config)
        self.rate_limiter = ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)
        seed_all(0)
        self.functions = [{
            "name": "view_files",
            "description": "Print out the file contents into the response to view.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files": {
                        "type": "array",
                        "description": "list of the files to view",
                        "items": {
                            "type": "string"  # assuming each file is represented as a string
                        }
                    },
                },
                "required": ["files"],
            },
        },
        {
            "name": "write_files",
            "description": "Write out multiple files. Use the diff format using line numbers, and it will be combined into the existing code base.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_and_contents": {
                        "type": "array",
                        "description": 'list of files and their contents in diff format using line numbers, each as a dictionary to write. When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is """+ 1: import time\n+ 2: import os""". Editing an existing line is """- 5: apple = 2 + 2\n+ 5: apple = 2 + 3""". Deleting a line is """- 5: apple = 2 + 2""".',
                        "items": {
                            "type": "object",
                            "properties": {
                                "file_path": {
                                    "type": "string",
                                    "description": "Path to the file"
                                },
                                "file_contents": {
                                    "type": "string",
                                    "description": "Contents of the file"
                                }
                            },
                            "required": ["file_path", "file_contents"]
                        }
                    }
                },
                "required": ["files_and_contents"],
            },
        },]
        self.messages = [{"role": "system", "content": f'''
Objective: Write code for a large system design task.

You must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task. 
         
When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is """+ 1: import time
+ 2: import os""". Editing an existing line is """- 5: apple = 2 + 2
+ 5: apple = 2 + 3""". Deleting a line is """- 5: apple = 2 + 2""".
                          
When modifying code and including new code, you must use the diff format using the line numbers.

Provide the minimal code necessary to achieve the task.

You cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.

You can write to local files, however you cannot use any databases, as none are setup in the local environment.
'''}]

    def test_selecting_right_files_and_adapting_them(self):
        code_repository_folder_file_path = "./test_suite/mock_data/chatbot-ui/"
        file_dict = load_code_files_into_dict(code_repository_folder_file_path)
        def view_files(files: [str]):
            return json.dumps({'files': format_files_into_prompt_format(file_dict, files)})
        available_functions = {'view_files': view_files}
        self.messages.append({"role": "user", "content": f"""
Objective: Take the existing code base and implement the following feature: Add a new button on the frontend that when clicked deletes all the chat histories and all the chat messages.
                              
There are the existing files in the code base, decide which ones you want to now view, to then adapt to implement this feature.
                              
{file_dict.keys()}
"""})
        response_message = self.get_llm_response()
        if response_message.get("function_call"):
            function_name = response_message["function_call"]["name"]
            fuction_to_call = available_functions[function_name]
            function_args = json.loads(response_message["function_call"]["arguments"])
            function_response = fuction_to_call(**function_args)
        self.messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )
        response_message = self.get_llm_response()
        self.messages.append({"role": "user", "content": f"""
Execute the first task
"""})
        response_message = self.get_llm_response()
        if response_message.get("function_call"):
            function_name = response_message["function_call"]["name"]
            fuction_to_call = available_functions[function_name]
            function_args = json.loads(response_message["function_call"]["arguments"])
            function_response = fuction_to_call(**function_args)
        self.messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )
        print(response_message['content'])




        # Assuming your agent's method to process and output code is named "process"
        output = self.agent.process(code_repository_folder_file_path, prompt)

        # Verify if the feature has been implemented.
        self.assertTrue(self.check_feature_implementation(output, "group chat"))

# class TestSummarizer(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         # This is run once before any tests or test methods in the class.
#         cls.agent = None

#     def test_group_chat_implementation(self):
#         code_repository_folder_file_path = "./mock_data/chatbot-ui/"

#         # Assuming your agent's method to process and output code is named "process"
#         output = 

#         # Verify if the feature has been implemented.
#         self.assertTrue(self.check_feature_implementation(output, "group chat"))

#     # ... More test methods ...

# Run the tests
if __name__ == '__main__':
    # unittest.main()
    # TestSystemDesignPromptChains().test_selecting_right_files_and_adapting_them()
    cls = TestSystemDesignPromptChains()
    cls.setUp()
    cls.test_selecting_right_files_and_adapting_them()