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

class TestSystemDesignPromptChains(unittest.TestCase):


    def get_llm_response(self, messages):
        # num_tokens = num_tokens_consumed_by_chat_request(messages=messages)
        logger = None
        name = "TestSystemDesignPromptChains"
        llm_config = get_llm_config(self.config, logger, name, self.rate_limiter)
        llm_config['messages'] = messages
        llm_config['temperature'] = 0.1
        llm_config['top_p'] = 1.0
        llm_config['functions'] = self.functions
        if messages[-1].get('function_call'):
            llm_config['function_call'] = messages[-1]['function_call']
            del(messages[-1]['function_call'])
        try:
            response = chat_completion_rl(**llm_config)
        except openai.error.InvalidRequestError as e:
            print("Error:", e.__dict__)  # or use a logging framework
            raise
        message_response = response["choices"][0]["message"]
        if not message_response.get('content'):
            message_response['content'] = None
        return message_response


    def setUp(self):
        # This is run once before any tests or test methods in the class.
        # Initialize Hydra
        initialize(config_path="config", version_base=None)  # Point to your actual config directory
        self.config = compose(config_name="config.yaml")
        self.max_tokens = get_model_max_tokens(self.config)
        request_limit, token_limit = setup_chat_rate_limiter(self.config)
        self.rate_limiter = ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)
        seed_all(0)
        self.functions = [
            {
            "name": "provide_detailed_sub_task_steps_for_sub_agents",
            "description": "Provide a list of strings, where each string details the sub-task step for a seperate sub-agent to complete.",
            "parameters": {
                "type": "object",
                "properties": {
                    "steps": {
                        "type": "array",
                        "description": "list of detailed the sub-task steps for a seperate sub-agent to complete.",
                        "items": {
                            "type": "string"  # assuming each file is represented as a string
                        }
                    },
                },
                "required": ["files"],
            },
            },
            {
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
        #     {
        #     "name": "search_for_relevant_files",
        #     "description": "Search for relevant files of code, given a query. Then print out the file names in the response view. This uses cosine similarity between the query vector embedding and the code vector embedding, where the results are ordered by best match.",
        #     "parameters": {
        #         "type": "object",
        #         "properties": {
        #             "query": {
        #                 "type": "string",
        #                 "description": "text query to search for relevant files of code. This uses cosine similarity between the query embedding and the code embedding."
        #             }
        #         },
        #         "required": ["query"]
        #     }
        # },
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
        },
        {
            "name": "delete_files",
            "description": "Delete files. Specify the file names, and these files will be deleted. If you specify the file name '-1' all files in the folder will be deleted.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files": {
                        "type": "array",
                        "description": "list of the files to delete. If you provide a file name of '-1' all files in the folder will be deleted.",
                        "items": {
                            "type": "string"  # assuming each file is represented as a string
                        }
                    },
                },
                "required": ["files"],
            },
            },]
        self.system_message = {"role": "system", "content": f'''
Objective: Write code for a large system design task.

You must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task. 
         
When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is """+ 1: import time
+ 2: import os""". Editing an existing line is """- 5: apple = 2 + 2
+ 5: apple = 2 + 3""". Deleting a line is """- 5: apple = 2 + 2""".
                          
When modifying code and including new code, you must use the diff format using the line numbers.

Provide the minimal code necessary to achieve the task.

You cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.

You can write to local files, however you cannot use any databases, as none are setup in the local environment.
                          
Use the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.
'''}

    def test_solve_a_system_design_task(self):
        # code_repository_folder_file_path = "./test_suite/mock_data/chatbot-ui/"
        # file_dict = load_code_files_into_dict(code_repository_folder_file_path)
        file_dict = {}
        # df = cache_or_compute('embed_all_code_files(file_dict)', embed_all_code_files, file_dict)
        def view_files(files: [str], file_dict: dict):
            return json.dumps({'files': format_files_into_prompt_format(file_dict, files)})
        # def search_for_relevant_code(query: str, df_with_embeddings: pd.DataFrame, return_results=20):
        #     query_embedding = cache_or_compute(f'embed_query({query})', embedding_rl, query)[0]
        #     df_with_embeddings['similarities'] = df_with_embeddings.embeddings.apply(lambda x: cosine_similarity(x, query_embedding))
        #     df_with_embeddings = df_with_embeddings.sort_values('similarities', ascending=False)
        #     file_names = df_with_embeddings.head(return_results)['file_path'].to_list()
        #     return json.dumps({'file_names': file_names})
        def write_files(files_and_contents: [dict], file_dict: dict):
            file_dict = implement_git_diff_on_file_dict(file_dict, files_and_contents)
            output = {
                "status": "success",
                "message": "write_files completed successfully."
            }
            return json.dumps(output), file_dict
        available_functions = {
            'view_files': view_files,
            # 'search_for_relevant_files': partial(search_for_relevant_code, df_with_embeddings=df),
            'write_files': write_files}
#         self.messages.append({"role": "user", "content": f"""
# Objective: Write complete python code for the following backend system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)
# Things to include: 
# * Approach for one-on-one text messaging between users.
# * Approach for extending the design to support group chats.
# * Delivered and read status
# * What action needs to be taken if the user is not connected to the internet?
# * Push notifications
# * Sending media like images or other documents
# * Approach for providing end-to-end message encryption.
                              
# Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once.
# """})
        self.messages.append({"role": "user", "content": f"""
You will get instructions for code to write.
You will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.

Think step by step and reason yourself to the right decisions to make sure we get it right.
First lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.

Do not comment on what every file does. Please note that the code should be fully functional. No placeholders.

You will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.
Please note that the code should be fully functional. No placeholders.

Follow a language and framework appropriate best practice file naming convention.
Make sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.
When writing code if you are unsure, write a plausible implementation.
Include module dependency or package manager dependency definition file.

Useful to know:
                              
Almost always put different classes in different files.
Always use the programming language the user asks for.
For Python, you always create an appropriate requirements.txt file.
For NodeJS, you always create an appropriate package.json file.
Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.


Python toolbelt preferences:
- pytest
- dataclasses
      
Objective: Write complete MVC code for the following system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)
Things to include: 
* Approach for one-on-one text messaging between users.
* Approach for extending the design to support group chats.
* Delivered and read status
* What action needs to be taken if the user is not connected to the internet?
* Push notifications
* Sending media like images or other documents
* Approach for providing end-to-end message encryption.

Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once.                              
"""})
        has_completed_task = False
        while not has_completed_task:
            response_message = self.get_llm_response()
            if response_message.get("content") and "ACCEPT" in response_message["content"]:
                has_completed_task = True
                break
            if response_message.get("function_call"):
                function_name = response_message["function_call"]["name"]
                function_args = json.loads(response_message["function_call"]["arguments"])
                fuction_to_call = available_functions[function_name]
                function_args['file_dict'] = file_dict
                if function_name == 'write_files':
                    function_response, file_dict = fuction_to_call(**function_args)
                else:
                    function_response = fuction_to_call(**function_args)
                self.messages.append(
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    }
                )
            else:
                self.messages.append({"role": "user", "content": f"""
Continue. If the overall task is complete return ACCEPT. If not continue.
"""})       
            num_tokens = num_tokens_consumed_by_chat_request(messages=self.messages, functions=self.functions)
            pretty_print_chat_messages(self.messages, num_tokens, self.max_tokens)
        self.messages.append({"role": "user", "content": f"""
Now write a ToDo.md file on what can be done to improve this code based on the original task given, and list out the steps to do it. This will be read by a new agent like you to improve and add more code to this code repository.
"""})       
        self.assertTrue(has_completed_task)

    def test_solve_a_system_design_task_splitting_steps(self):
        # code_repository_folder_file_path = "./test_suite/mock_data/chatbot-ui/"
        # file_dict = load_code_files_into_dict(code_repository_folder_file_path)
        file_dict = {}
        # df = cache_or_compute('embed_all_code_files(file_dict)', embed_all_code_files, file_dict)
        def view_files(files: [str], file_dict: dict):
            return json.dumps({'files': format_files_into_prompt_format(file_dict, files)})
        # def search_for_relevant_code(query: str, df_with_embeddings: pd.DataFrame, return_results=20):
        #     query_embedding = cache_or_compute(f'embed_query({query})', embedding_rl, query)[0]
        #     df_with_embeddings['similarities'] = df_with_embeddings.embeddings.apply(lambda x: cosine_similarity(x, query_embedding))
        #     df_with_embeddings = df_with_embeddings.sort_values('similarities', ascending=False)
        #     file_names = df_with_embeddings.head(return_results)['file_path'].to_list()
        #     return json.dumps({'file_names': file_names})
        def provide_detailed_sub_task_steps_for_sub_agents(steps: [str]):
            return steps
        def write_files(files_and_contents: [dict], file_dict: dict):
            file_dict = implement_git_diff_on_file_dict(file_dict, files_and_contents)
            output = {
                "status": "success",
                "message": "write_files completed successfully."
            }
            return json.dumps(output), file_dict
        available_functions = {
            'view_files': view_files,
            # view file names.
            # 'search_for_relevant_files': partial(search_for_relevant_code, df_with_embeddings=df),
            'provide_detailed_sub_task_steps_for_sub_agents': provide_detailed_sub_task_steps_for_sub_agents,
            'write_files': write_files}
        meta_messages = [self.system_message]
        meta_messages.append({"role": "user", "content": f"""
You will get instructions for code to write.
You will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.

Think step by step and reason yourself to the right decisions to make sure we get it right.
First lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.

Do not comment on what every file does. Please note that the code should be fully functional. No placeholders.

You will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.
Please note that the code should be fully functional. No placeholders.

Follow a language and framework appropriate best practice file naming convention.
Make sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.
When writing code if you are unsure, write a plausible implementation.
Include module dependency or package manager dependency definition file.

Useful to know:
                              
Almost always put different classes in different files.
Always use the programming language the user asks for.
For Python, you always create an appropriate requirements.txt file.
For NodeJS, you always create an appropriate package.json file.
Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.


Python toolbelt preferences:
- pytest
- dataclasses
      
Objective: Write complete MVC code for the following system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)
Things to include: 
* Approach for one-on-one text messaging between users.
* Approach for extending the design to support group chats.
* Delivered and read status
* What action needs to be taken if the user is not connected to the internet?
* Push notifications
* Sending media like images or other documents
* Approach for providing end-to-end message encryption.

Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once. Only create a detailed plan to begin with.                              
"""})
        has_completed_task = False
        response_message = self.get_llm_response(meta_messages)
        meta_messages.append(response_message)
        num_tokens = num_tokens_consumed_by_chat_request(messages=meta_messages, functions=self.functions)
        pretty_print_chat_messages(meta_messages, num_tokens, self.max_tokens)
        meta_messages.append({"role": "user", "content": f"""
Reflect and improve this plan, adding more details for each step, such that each step can be given to seperate agent identical to yourself to complete and return the code for that step.
""", "function_call": {"name": "provide_detailed_sub_task_steps_for_sub_agents"}})
        response_message = self.get_llm_response(meta_messages)
        meta_messages.append(response_message)
        num_tokens = num_tokens_consumed_by_chat_request(messages=meta_messages, functions=self.functions)
        pretty_print_chat_messages(meta_messages, num_tokens, self.max_tokens)
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])
        fuction_to_call = available_functions[function_name]
        steps = fuction_to_call(**function_args)
        for step in steps:
            sub_messages = deepcopy(meta_messages)
            sub_messages.append({"role": "user", "content": f"""
Execute step: {step} \n\n Condition it on existing code: {list(file_dict.keys())}
"""})
            has_completed_sub_step = False
            while not has_completed_sub_step:
                response_message = self.get_llm_response(sub_messages)
                sub_messages.append(response_message)
                if response_message.get("content") and "ACCEPT" in response_message["content"]:
                    has_completed_sub_step = True
                    break
                if response_message.get("function_call"):
                    function_name = response_message["function_call"]["name"]
                    function_args = json.loads(response_message["function_call"]["arguments"])
                    fuction_to_call = available_functions[function_name]
                    function_args['file_dict'] = file_dict
                    if function_name == 'write_files':
                        function_response, file_dict = fuction_to_call(**function_args)
                    else:
                        function_response = fuction_to_call(**function_args)
                    sub_messages.append(
                        {
                            "role": "function",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                sub_messages.append({"role": "user", "content": f"""
Has the task been completed of: ```
{step}
``` \n\n If yes, return ACCEPT, otherwise reflect and return the full complete corrected code to complete the task, use the defined functions to write the code.
"""})
                num_tokens = num_tokens_consumed_by_chat_request(messages=sub_messages, functions=self.functions)
                pretty_print_chat_messages(sub_messages, num_tokens, self.max_tokens)
            print('sub step completed')
        print('All steps complete')
        meta_messages.append({"role": "user", "content": f"""
Sub tasks completed successfully. I will now give you all the generated files. Please list out further steps to successfully fully complete the task.
"""})
        meta_messages.append(
                        {
                            "role": "function",
                            "name": "view_files",
                            "content": view_files(list(file_dict.keys()), file_dict),
                        }
                    )


        meta_messages.append({"role": "user", "content": f"""
Please list out further steps to successfully fully complete the task. Adding details for each step, such that each step can be given to seperate agent identical to yourself to complete and return the code for that step.
""", "function_call": {"name": "provide_detailed_sub_task_steps_for_sub_agents"}})
        response_message = self.get_llm_response(meta_messages)
        meta_messages.append(response_message)
        num_tokens = num_tokens_consumed_by_chat_request(messages=meta_messages, functions=self.functions)
        pretty_print_chat_messages(meta_messages, num_tokens, self.max_tokens)
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])
        fuction_to_call = available_functions[function_name]
        steps = fuction_to_call(**function_args)
        for step in steps:
            sub_messages = deepcopy(meta_messages)
            sub_messages.append({"role": "user", "content": f"""
Execute step: {step} \n\n Condition it on existing code: {list(file_dict.keys())}
"""})
            has_completed_sub_step = False
            while not has_completed_sub_step:
                response_message = self.get_llm_response(sub_messages)
                sub_messages.append(response_message)
                if response_message.get("content") and "ACCEPT" in response_message["content"]:
                    has_completed_sub_step = True
                    break
                if response_message.get("function_call"):
                    function_name = response_message["function_call"]["name"]
                    function_args = json.loads(response_message["function_call"]["arguments"])
                    fuction_to_call = available_functions[function_name]
                    function_args['file_dict'] = file_dict
                    if function_name == 'write_files':
                        function_response, file_dict = fuction_to_call(**function_args)
                    else:
                        function_response = fuction_to_call(**function_args)
                    sub_messages.append(
                        {
                            "role": "function",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                sub_messages.append({"role": "user", "content": f"""
Has the task been completed of: ```
{step}
``` \n\n If yes, return ACCEPT, otherwise reflect and return the full complete corrected code to complete the task, use the defined functions to write the code.
"""})
                num_tokens = num_tokens_consumed_by_chat_request(messages=sub_messages, functions=self.functions)
                pretty_print_chat_messages(sub_messages, num_tokens, self.max_tokens)
            print('sub step completed')
        print('All steps complete')
        fin_messages = deepcopy(meta_messages)
        fin_messages.append(
                        {
                            "role": "function",
                            "name": "view_files",
                            "content": view_files(list(file_dict.keys()), file_dict),
                        }
                    )


        num_tokens = num_tokens_consumed_by_chat_request(messages=fin_messages, functions=self.functions)
        pretty_print_chat_messages(fin_messages, num_tokens, self.max_tokens)
        

        self.messages.append({"role": "user", "content": f"""
Now write a ToDo.md file on what can be done to improve this code based on the original task given, and list out the steps to do it. This will be read by a new agent like you to improve and add more code to this code repository.
"""})       

        self.assertTrue(has_completed_task)



    def test_improve_generated_code_base(self):
        # code_repository_folder_file_path = "./test_suite/mock_data/chatbot-ui/"
        # file_dict = load_code_files_into_dict(code_repository_folder_file_path)
        from examples.chat_app import file_dict_with_to_do as file_dict
        # df = cache_or_compute('embed_all_code_files(file_dict)', embed_all_code_files, file_dict)
        def view_files(files: [str], file_dict: dict):
            return json.dumps({'files': format_files_into_prompt_format(file_dict, files)})
        # def search_for_relevant_code(query: str, df_with_embeddings: pd.DataFrame, return_results=20):
        #     query_embedding = cache_or_compute(f'embed_query({query})', embedding_rl, query)[0]
        #     df_with_embeddings['similarities'] = df_with_embeddings.embeddings.apply(lambda x: cosine_similarity(x, query_embedding))
        #     df_with_embeddings = df_with_embeddings.sort_values('similarities', ascending=False)
        #     file_names = df_with_embeddings.head(return_results)['file_path'].to_list()
        #     return json.dumps({'file_names': file_names})
        def write_files(files_and_contents: [dict], file_dict: dict):
            file_dict = implement_git_diff_on_file_dict(file_dict, files_and_contents)
            output = {
                "status": "success",
                "message": "write_files completed successfully."
            }
            return json.dumps(output), file_dict
        available_functions = {
            'view_files': view_files,
            # 'search_for_relevant_files': partial(search_for_relevant_code, df_with_embeddings=df),
            'write_files': write_files}
#         self.messages.append({"role": "user", "content": f"""
# Objective: Write complete python code for the following backend system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)
# Things to include: 
# * Approach for one-on-one text messaging between users.
# * Approach for extending the design to support group chats.
# * Delivered and read status
# * What action needs to be taken if the user is not connected to the internet?
# * Push notifications
# * Sending media like images or other documents
# * Approach for providing end-to-end message encryption.
                              
# Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once.
# """})
        ToDoContents = '\n'.join(remove_line_numbers(file_dict['ToDo.md']))
        self.messages.append({"role": "user", "content": f"""
You will get instructions for code to write.
You will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.

Think step by step and reason yourself to the right decisions to make sure we get it right.
First lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.

Do not comment on what every file does. Please note that the code should be fully functional. No placeholders.

You will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.
Please note that the code should be fully functional. No placeholders.

Follow a language and framework appropriate best practice file naming convention.
Make sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.
When writing code if you are unsure, write a plausible implementation.
Include module dependency or package manager dependency definition file.

Useful to know:
                              
Almost always put different classes in different files.
Always use the programming language the user asks for.
For Python, you always create an appropriate requirements.txt file.
For NodeJS, you always create an appropriate package.json file.
Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.


Python toolbelt preferences:
- pytest
- dataclasses
      
Objective: Take the existing code base and implement the following ToDo features.
                              
The original code base was implemented to fufill the task of: Write complete MVC code for the following system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)
Things to include: 
* Approach for one-on-one text messaging between users.
* Approach for extending the design to support group chats.
* Delivered and read status
* What action needs to be taken if the user is not connected to the internet?
* Push notifications
* Sending media like images or other documents
* Approach for providing end-to-end message encryption.
                              
ToDo.md
```markdown
{ToDoContents}
```

There are the existing files in the code base of: {file_dict.keys()}
                              

Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once.                              
"""})
        has_completed_task = False
        while not has_completed_task:
            response_message = self.get_llm_response()
            if response_message.get("content") and "ACCEPT" in response_message["content"]:
                has_completed_task = True
                break
            if response_message.get("function_call"):
                function_name = response_message["function_call"]["name"]
                function_args = json.loads(response_message["function_call"]["arguments"])
                fuction_to_call = available_functions[function_name]
                function_args['file_dict'] = file_dict
                if function_name == 'write_files':
                    function_response, file_dict = fuction_to_call(**function_args)
                else:
                    function_response = fuction_to_call(**function_args)
                self.messages.append(
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    }
                )
            else:
                self.messages.append({"role": "user", "content": f"""
Continue. If the overall task is complete return ACCEPT. If not continue.
"""})       
            num_tokens = num_tokens_consumed_by_chat_request(messages=self.messages, functions=self.functions)
            pretty_print_chat_messages(self.messages, num_tokens, self.max_tokens)
        self.messages.append({"role": "user", "content": f"""
Now write a ToDo.md file on what can be done to improve this code based on the original task given, and list out the steps to do it. This will be read by a new agent like you to improve and add more code to this code repository.
"""})       
        self.assertTrue(has_completed_task)





    def test_selecting_right_files_and_adapting_them(self):
        code_repository_folder_file_path = "./test_suite/mock_data/chatbot-ui/"
        file_dict = load_code_files_into_dict(code_repository_folder_file_path)
        df = cache_or_compute('embed_all_code_files(file_dict)', embed_all_code_files, file_dict)
        def view_files(files: [str], file_dict: dict):
            return json.dumps({'files': format_files_into_prompt_format(file_dict, files)})
        def search_for_relevant_code(query: str, df_with_embeddings: pd.DataFrame, return_results=20):
            query_embedding = cache_or_compute(f'embed_query({query})', embedding_rl, query)[0]
            df_with_embeddings['similarities'] = df_with_embeddings.embeddings.apply(lambda x: cosine_similarity(x, query_embedding))
            df_with_embeddings = df_with_embeddings.sort_values('similarities', ascending=False)
            file_names = df_with_embeddings.head(return_results)['file_path'].to_list()
            return json.dumps({'file_names': file_names})
        def write_files(files_and_contents: [dict], file_dict: dict):
            file_dict = implement_git_diff_on_file_dict(file_dict, files_and_contents)
            output = {
                "status": "success",
                "message": "write_files completed successfully."
            }
            return json.dumps(output)
        available_functions = {
            'view_files': partial(view_files, file_dict=file_dict),
            'search_for_relevant_files': partial(search_for_relevant_code, df_with_embeddings=df),
            'write_files': partial(write_files, file_dict=file_dict)}
        self.messages.append({"role": "user", "content": f"""
Objective: Take the existing code base and implement the following feature: Add a new button on the frontend that when clicked deletes all the chat histories and all the chat messages.

Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once.
                              
There are the existing files in the code base of: {file_dict.keys()}
"""})
        has_completed_task = False
        while not has_completed_task:
            response_message = self.get_llm_response()
            if response_message.get("content") and "ACCEPT" in response_message["content"]:
                has_completed_task = True
                break
            if response_message.get("function_call"):
                function_name = response_message["function_call"]["name"]
                function_args = json.loads(response_message["function_call"]["arguments"])
                fuction_to_call = available_functions[function_name]
                function_response = fuction_to_call(**function_args)
                self.messages.append(
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    }
                )
            else:
                self.messages.append({"role": "user", "content": f"""
Execute task. If complete return ACCEPT. If not continue.
"""})       
            num_tokens = num_tokens_consumed_by_chat_request(messages=self.messages, functions=self.functions)
            pretty_print_chat_messages(self.messages, num_tokens, self.max_tokens)
        self.assertTrue(has_completed_task)

# Run the tests
if __name__ == '__main__':
    # unittest.main()
    # TestSystemDesignPromptChains().test_selecting_right_files_and_adapting_them()
    cls = TestSystemDesignPromptChains()
    cls.setUp()
    # cls.test_solve_a_system_design_task()
    cls.test_solve_a_system_design_task_splitting_steps()
    # cls.test_improve_generated_code_base()