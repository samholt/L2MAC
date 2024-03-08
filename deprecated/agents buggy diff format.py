import wandb
import random
import numpy as np
import openai
from llm_utils import chat_completion_rl
import re
from torch.multiprocessing import Queue
import json
from copy import deepcopy
from llm_utils import get_llm_config
from llm_utils import setup_chat_rate_limiter, chat_completion_rl, get_llm_config, num_tokens_consumed_by_chat_request, get_model_max_tokens, embedding_rl, pretty_print_chat_messages
from utils.llm_tools import available_functions
from summarizer_and_modifier import add_line_numbers, write_files_from_dict
from openai.error import InvalidRequestError
from pathlib import Path

def get_code_from_message(message):
    match = re.search(r'```python\n(.*?)\n```', message, re.DOTALL)
    if match:
        code = match.group(1)
    else:
        match = re.search(r'``` python\n(.*?)\n```', message, re.DOTALL)
        if match:
            code = match.group(1)
        else:
            match = re.search(r'```(.*?)```', message, re.DOTALL)
            if match:
                code = match.group(1)
            else:
                code = None
    return code

def initialize_agent(method_name, env, config, rate_limiter, wandb_project_name=None, logger=None):
    # Initialize Weights & Biases if a project name is provided
    if wandb_project_name:
        wandb.init(project=wandb_project_name, config=config)

    # Depending on the method name, initialize the agent
    if method_name == "human":
        agent = HumanAgent(env, config, logger, rate_limiter)
    elif method_name == "zero_shot":
        agent = ZeroShotAgent(env, config, logger, rate_limiter)
    elif method_name == "LLMatic":
        agent = LLMatic(env, config, logger, rate_limiter)
    else:
        raise ValueError(f"Unknown method name: {method_name}")

    return agent

class Agent:
    def __init__(self, env, config, logger, rate_limiter):
        self.env = env
        self.config = config
        self.seed_value = None
        self.logger = logger
        self.rate_limiter = rate_limiter

    def run(self, state):
        raise NotImplementedError("Agents must implement a run method.")

    def seed(self, seed_value):
        self.seed_value = seed_value
        random.seed(seed_value)
        np.random.seed(seed_value)
    
    def get_llm_config(self):
        return get_llm_config(self.config, self.logger, self.name, self.rate_limiter)




# class ZeroShotAgent(Agent):
#     def __init__(self, env, config, logger, rate_limiter):
#         super().__init__(env, config, logger, rate_limiter)
#         self.name = 'zero_shot'

#     def run(self, state):
#         llm_config = self.get_llm_config()
#         prompt = self.env.create_baseline_prompt()
# #         zero_shot_prompt = f'''
# # Objective: Write python code for a data science pipeline task to achieve the highest classification accuracy possible.

# # The code written should import all libraries you are to use, and should have the function ```def train_model(X_train: DataFrame, y_train: ndarray) -> Tuple[BaseEstimator, ColumnTransformer]:```.  This function runs the data science pipeline. This involves processing X_train, and returning a tuple of the trained model and a preprocessor used for preprocessing the input features.

# # You cannot load or write any external data. You only have access to the data given in the function `train_model`. Only provide the function and library imports, do not include any example code on how to use the function.

# # Return code only in ``` backticks.

# # The X_train dataframe has the following column names: {state}'''
#         llm_config['messages'] = [
#                         {"role": "system", "content": "You are an automated expert data scientist. You write code only in Python."},
#                         {"role": "user", "content": zero_shot_prompt},
#                     ]
#         response = chat_completion_rl(**llm_config)
#         text = response['choices'][0]['message']['content']
#         match = re.search(r'```python\n(.*?)\n```', text, re.DOTALL)
#         if match:
#             code = match.group(1)
#         else:
#             match = re.search(r'``` python\n(.*?)\n```', text, re.DOTALL)
#             if match:
#                 code = match.group(1)
#             else:
#                 match = re.search(r'```(.*?)```', text, re.DOTALL)
#                 if match:
#                     code = match.group(1)
#                 else:
#                     code = None
#                     raise ValueError(f"Could not find code in response: {text}")
#         action = code
#         return action
    
class LLMatic(Agent):
    def __init__(self, env, config, logger, rate_limiter):
        super().__init__(env, config, logger, rate_limiter)
        self.name = 'LLMatic'
        # self.load_from_checkpoint = 'logs/run-20230919-125955_zero_shot-LLMatic_donnemartin|system-design|oop|url_shortener-donnemartin|system-design|oop|whatsapp-donnemartin|system-design|oop|twitter_0_3-runs_log/url_shortener/0/LLMatic_state_beginning_step_3.json'
        self.load_from_checkpoint = ''
        # self.replay_llm_responses_path = 'logs/run-20230919-135327_LLMatic_donnemartin|system-design|oop|url_shortener-donnemartin|system-design|oop|whatsapp-donnemartin|system-design|oop|twitter_0_3-runs_log/url_shortener/0/LLMatic_llm_responses.json'
        # self.replay_llm_responses_path = 'logs/run-20230919-140115_LLMatic_donnemartin|system-design|oop|url_shortener-donnemartin|system-design|oop|whatsapp-donnemartin|system-design|oop|twitter_0_3-runs_log/url_shortener/0/LLMatic_llm_responses.json'
        self.replay_llm_responses_path = ''
        self.replay_llm_responses_path_index = 0
        self.responses = []
        if self.load_from_checkpoint:
            with open(self.load_from_checkpoint, 'r') as f:
                data = json.load(f)
            self.file_dict = data['file_dict']
            self.steps = data['steps']
            self.step = data['step']
            self.meta_messages = data['meta_messages']
            self.base_dialog = data['base_dialog']
            self.sub_messages = data['sub_messages']
            self.responses = data['responses']
        else:
            self.file_dict = {}
            self.steps = []
            self.step = None
            self.meta_messages = []
            self.base_dialog = []
            self.sub_messages = []
            self.responses = []
        
        write_files_from_dict(self.file_dict)

        self.folder_path = f"{self.config.run.log_path.split('.txt')[0]}/{self.env.env_task_id}/{self.env.seed}/"
        Path(self.folder_path).mkdir(parents=True, exist_ok=True)
        self.max_tokens = get_model_max_tokens(config)
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
            {
            "name": "list_files",
            "description": "Print out all the file names into the response to view.",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder_path": {
                        "type": "string",
                        "description": "folder path to view. Default is the root folder.",
                    },
                },
            },
            },
            {
            "name": "run_python_file",
            "description": "Run python file and return the output to the response to view. That is with 'python3 file_name_to_run'.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name_to_run": {
                        "type": "string",
                        "description": "file name to run",
                    },
                    "arguments": {
                        "type": "array",
                        "description": "optional run arguments",
                        "items": {
                            "type": "string"
                        }
                    },
                },
                "required": ["file_name_to_run"],
            },
            },
            {
            "name": "pytest_files",
            "description": "Run pytest on the input file names and print out the results to the response to view. If no file names are provided, pytest runs on all files.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_to_test": {
                        "type": "array",
                        "description": "file names to run pytest on",
                        "items": {
                            "type": "string"
                        }
                    },
                },
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
            "description": "Write out multiple files. Use the diff format using line numbers, and it will be combined into the existing code base. You always indent code with tabs. You always prefer to overwrite the complete file instead of making multiple changes to the same file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_and_contents": {
                        "type": "array",
                        "description": 'list of files and their contents in diff format using line numbers, each as a dictionary to write. When writing any code you will always give it in diff format, with line numbers. For example. Replacing a line is """r 8: def fruit(name):""". Deleting multiple lines from line 5 to 10 is """- 5-10""". Appending two new lines to a file at specified line numbers is """+ 5: import time\n+ 6: import os""". If you wish to overwrite the existing file (delete it completely and then add the new lines), please specify overwrite_file to True.',
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
                                },
                                "overwrite_file": {
                                    "type": "boolean",
                                    "description": "Overwrite the existing file"
                                }
                            },
                            "required": ["file_path", "file_contents", "overwrite_file"]
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

You must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task, and correctly incorporate it into the existing code base.

When writing any code you will always give it in diff format, with line numbers. For example.
For example. Replacing a line is """r 8: def fruit(name):""". Deleting multiple lines from line 5 to 10 is """- 5-10""". Appending two new lines to a file is """+ 5: import time\n+ 6: import os""". If you wish to overwrite the existing file (delete it completely and then add the new lines), please specify overwrite_file to True.
You always indent code with tabs.

When modifying code and including new code, you must use the diff format using the line numbers.
Please always view the files before writing to them, to make sure you are writing to the correct files.
If you are unsure, you can list all available files to view with the `list_files` function.

Provide the minimal code necessary to achieve the task conditioned on the existing generated code---including changing the existing generated code.

You cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.

You can write to local files, however you cannot use any databases, as none are setup in the local environment.

Use the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.
'''}

    def print_dialog(self, messages):
        num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
        pretty_print_chat_messages(messages, num_tokens, self.max_tokens)

    def save_agent_state(self, messages, beginning_step=''):
        data_to_save = {'messages': messages,
                        'file_dict': self.file_dict,
                        'steps': self.steps,
                        'step': self.step,
                        'meta_messages': self.meta_messages,
                        'base_dialog': self.base_dialog,
                        'sub_messages': self.sub_messages,
                        }
        if not beginning_step:
            path = f'{self.folder_path}current_LLMatic_state.json' 
        else:
            step_number = beginning_step.split('.')[0]
            path = f'{self.folder_path}LLMatic_state_beginning_step_{step_number}.json'
        with open(path, 'w') as f:
            json.dump(data_to_save, f)

    def get_llm_response(self, messages):
        self.print_dialog(messages)
        self.save_agent_state(messages)
        llm_config = self.get_llm_config()
        llm_config['messages'] = messages
        llm_config['functions'] = self.functions
        if messages[-1].get('function_call'):
            llm_config['function_call'] = messages[-1]['function_call']
            del(messages[-1]['function_call'])
        if self.replay_llm_responses_path:
            with open(self.replay_llm_responses_path, 'r') as f:
                responses = json.load(f)
            response = responses[self.replay_llm_responses_path_index]
            self.replay_llm_responses_path_index += 1
        else:
            try:
                response = chat_completion_rl(**llm_config)
                self.responses.append(response)
                with open(f'{self.folder_path}LLMatic_llm_responses.json', 'w') as f:
                    json.dump(self.responses, f)
            except openai.error.InvalidRequestError as e:
                print("Error:", e.__dict__)  # or use a logging framework
                raise
        message_response = response["choices"][0]["message"]
        if not message_response.get('content'):
            message_response['content'] = None
        return message_response

    def run(self, state=''):
        # try:
        self._run(state)
        # except Exception as e:
        #     print(e)
        #     print('Error in LLMatic')
        #     print('')
        #     print('Saving state')
        #     self.save_agent_state(self.sub_messages)
        #     raise e


    def _run(self, state=''):
        if not self.load_from_checkpoint:
            # unit_tests = self.env.ut
            # self.file_dict['test_all.py'] = add_line_numbers(unit_tests.split('\n'))
            self.meta_messages = [self.system_message]
            task_description = self.env.desc
            self.meta_messages.append({"role": "user", "content": f"""
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

Always use the programming language the user asks for.
For Python, you always create an appropriate requirements.txt file.
For NodeJS, you always create an appropriate package.json file.
Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.
You can use any package and any other packages you wish to install.

Python toolbelt preferences:
- pytest
- dataclasses

Objective:```
{task_description}
```

Understand the problem, by creating a detailed step-by-step plan. Try to solve the problem in the minimal steps necessary, in no more than 10 steps. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation, where all the code is fully functional. Use best software design practices, and you can output large amounts of code at once. The last step should be running any tests automatically if they exist, and the penultimate step writing these tests. You will receive no human input at any stage, so you cannot use a human to test. Only create a detailed plan to begin with, which includes designing and running tests to check that they all pass.
"""})
            has_completed_task = False
            initial_response_message = self.get_llm_response(self.meta_messages)
            current_dialog = deepcopy(self.meta_messages)
            current_dialog.append(initial_response_message)
            # current_dialog.append({"role": "user", "content": f"""Reflect and improve this plan, adding more details for each step, such that each step can be given to seperate agent identical to yourself to complete and return the code for that step.""", "function_call": {"name": "provide_detailed_sub_task_steps_for_sub_agents"}})
            # second_response_message = self.get_llm_response(current_dialog)
            # current_dialog = deepcopy(self.meta_messages)
            # current_dialog.append(second_response_message)
            # function_name = second_response_message["function_call"]["name"]
            # function_args = json.loads(second_response_message["function_call"]["arguments"])
            function_name = initial_response_message["function_call"]["name"]
            function_args = json.loads(initial_response_message["function_call"]["arguments"])
            fuction_to_call = available_functions[function_name]
            self.steps = fuction_to_call(**function_args)
            self.print_dialog(current_dialog)
            self.base_dialog = deepcopy(current_dialog)
        else:
            step_index = self.steps.index(self.step)
            self.steps = self.steps[step_index:]
            self.base_dialog[0] = self.system_message
            self.meta_messages[0] = self.system_message
        for step in self.steps:
            self.step = deepcopy(step)
            self.sub_messages = deepcopy(self.base_dialog)
            self.save_agent_state(self.sub_messages, beginning_step=self.step)
            self.sub_messages.append({"role": "user", "content": f"""
Objective: Execute task step: {step} \n\n Note: Condition any new code files on the existing code files: {list(self.file_dict.keys())}. You can now optionally view the existing files if you need to view them to complete the current task step. You have a limited context window so be selective about which files you view, only view the files you think you might need to view.
"""})
            has_completed_sub_step = False
            max_re_tries = 10
            re_tries = 0
            while not has_completed_sub_step:
                try:
                    response_message = self.get_llm_response(self.sub_messages)
                except InvalidRequestError as e:
                    if 'maximum context' in e.args[0]:
                        re_tries += 1
                        if re_tries > max_re_tries:
                            raise e
                        # Restart the step. Should control re-try times.
                        self.sub_messages = deepcopy(self.base_dialog)
                        self.sub_messages.append({"role": "user", "content": f"""
Objective: Execute task step: {step} \n\n Note: Condition any new code files on the existing code files: {list(self.file_dict.keys())}. You can now optionally view the existing files if you need to view them to complete the current task step. You have a limited context window so be selective about which files you view, only view the files you think you might need to view.
"""})
                        response_message = self.get_llm_response(self.sub_messages)              
                if response_message.get("content") and "ACCEPT" in response_message["content"]:
                    has_completed_sub_step = True
                    break
                if response_message.get("function_call"):
                    function_name = response_message["function_call"]["name"]
                    try:
                        function_args = json.loads(response_message["function_call"]["arguments"])
                    except json.decoder.JSONDecodeError:
                        function_args = {}
                        continue
                    fuction_to_call = available_functions[function_name]
                    function_args['file_dict'] = self.file_dict
                    if function_name == 'write_files':
                        function_response, self.file_dict = fuction_to_call(**function_args)
                    else:
                        function_response = fuction_to_call(**function_args)
                    self.sub_messages.append(response_message)
                    self.sub_messages.append(
                        {
                            "role": "function",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                else:
                    self.sub_messages.append(response_message)
                self.sub_messages.append({"role": "user", "content": f"""
Has the task been completed of: ```
{step}
``` \n\n If yes, return ACCEPT, otherwise reflect and return the full complete corrected code to complete the task, use the defined functions to write the code. Condition it on existing code: {list(self.file_dict.keys())}. If you have not viewed the files before writing to them, please view them, to make sure you are writing to the correct files.
"""})
                self.print_dialog(self.sub_messages)
                write_files_from_dict(self.file_dict)
            print('sub step completed')
        print('All steps complete')
        print('')
        write_files_from_dict(self.file_dict, base_dir=f'{self.folder_path}/{self.name}/files')
        self.save_agent_state(self.sub_messages)

    
class ZeroShotAgent(Agent):
    def __init__(self, env, config, logger, rate_limiter):
        super().__init__(env, config, logger, rate_limiter)
        self.name = 'ZeroShot'
        self.load_from_checkpoint = ''
        if self.load_from_checkpoint:
            with open(self.load_from_checkpoint, 'r') as f:
                data = json.load(f)
            self.file_dict = data['file_dict']
            self.steps = data['steps']
            self.step = data['step']
            self.meta_messages = data['meta_messages']
            self.base_dialog = data['base_dialog']
            self.sub_messages = data['sub_messages']
        else:
            self.file_dict = {}
            self.steps = []
            self.step = None
            self.meta_messages = []
            self.base_dialog = []
            self.sub_messages = []
        
        write_files_from_dict(self.file_dict)

        self.folder_path = f"{self.config.run.log_path.split('.txt')[0]}/{self.env.env_task_id}/{self.env.seed}/"
        Path(self.folder_path).mkdir(parents=True, exist_ok=True)
        self.max_tokens = get_model_max_tokens(config)
        self.functions = [
            # {
            # "name": "provide_detailed_sub_task_steps_for_sub_agents",
            # "description": "Provide a list of strings, where each string details the sub-task step for a seperate sub-agent to complete.",
            # "parameters": {
            #     "type": "object",
            #     "properties": {
            #         "steps": {
            #             "type": "array",
            #             "description": "list of detailed the sub-task steps for a seperate sub-agent to complete.",
            #             "items": {
            #                 "type": "string"  # assuming each file is represented as a string
            #             }
            #         },
            #     },
            #     "required": ["files"],
            # },
            # },
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
            {
            "name": "list_files",
            "description": "Print out all the file names into the response to view.",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder_path": {
                        "type": "string",
                        "description": "folder path to view. Default is the root folder.",
                    },
                },
            },
            },
            {
            "name": "run_python_file",
            "description": "Run python file and return the output to the response to view. That is with 'python3 file_name_to_run'.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name_to_run": {
                        "type": "string",
                        "description": "file name to run",
                    },
                    "arguments": {
                        "type": "array",
                        "description": "optional run arguments",
                        "items": {
                            "type": "string"
                        }
                    },
                },
                "required": ["file_name_to_run"],
            },
            },
            {
            "name": "pytest_files",
            "description": "Run pytest on the input file names and print out the results to the response to view. If no file names are provided, pytest runs on all files.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_to_test": {
                        "type": "array",
                        "description": "file names to run pytest on",
                        "items": {
                            "type": "string"
                        }
                    },
                },
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
            "description": "Write out multiple files. Use the diff format using line numbers, and it will be combined into the existing code base. You always delete all lines first before adding new lines.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_and_contents": {
                        "type": "array",
                        "description": 'list of files and their contents in diff format using line numbers, each as a dictionary to write. When writing any code you will always give it in diff format, with line numbers. For example. Adding two new lines to a new file is """+ 1: import time\n+ : import os""". Deleting a multiple lines from line 5 to 10 is """- 5-10""".',
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

You must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task, and correctly incorporate it into the existing code base.
         
When writing any code you will always give it in diff format, with line numbers. For example.
Adding two new lines to a new file is """+ 1: import time\n+ : import os""".
Deleting a multiple lines from line 5 to 10 is """- 5-10""".
                          
When modifying code and including new code, you must use the diff format using the line numbers.

Provide the minimal code necessary to achieve the task conditioned on the existing generated code---including changing the existing generated code.

You cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.

You can write to local files, however you cannot use any databases, as none are setup in the local environment.
                          
Use the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.
'''}

    def print_dialog(self, messages):
        num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
        pretty_print_chat_messages(messages, num_tokens, self.max_tokens)

    def save_agent_state(self, messages, beginning_step=''):
        data_to_save = {'messages': messages,
                        'file_dict': self.file_dict,
                        'steps': self.steps,
                        'step': self.step,
                        'meta_messages': self.meta_messages,
                        'base_dialog': self.base_dialog,
                        'sub_messages': self.sub_messages,
                        }
        if not beginning_step:
            path = f'{self.folder_path}current_ZeroShot_state.json' 
        else:
            step_number = beginning_step.split('.')[0]
            path = f'{self.folder_path}ZeroShot_state_beginning_step_{step_number}.json'
        with open(path, 'w') as f:
            json.dump(data_to_save, f)

    def get_llm_response(self, messages):
        self.print_dialog(messages)
        self.save_agent_state(messages)
        llm_config = self.get_llm_config()
        llm_config['messages'] = messages
        llm_config['max_tokens'] = 5000
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

    def run(self, state=''):
        try:
            self.meta_messages = [self.system_message]
            task_description = self.env.desc
            self.meta_messages.append({"role": "user", "content": f"""
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
                        
Always use the programming language the user asks for.
For Python, you always create an appropriate requirements.txt file.
For NodeJS, you always create an appropriate package.json file.
Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.


Python toolbelt preferences:
- pytest
- dataclasses

Objective:```
{task_description}
```
                        
Understand the problem, by creating a detailed step-by-step plan. Try to solve the problem in the minimal steps necessary. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once. Only create a detailed plan to begin with, which includes designing and running tests to check that they all pass.

First only respond with a list of all the steps.
""", "function_call": "none"})
            initial_response_message = self.get_llm_response(self.meta_messages)
            self.sub_messages = deepcopy(self.meta_messages)
            self.sub_messages.append(initial_response_message)
            self.sub_messages.append({"role": "user", "content": f"""
Now respond with all the code for the task in one response.
""", "function_call": {"name": "write_files"}})
            try:
                response_message = self.get_llm_response(self.sub_messages)
            except InvalidRequestError as e:
                if 'maximum context' in e.args[0]:
                    raise e          
            if response_message.get("function_call"):
                function_name = response_message["function_call"]["name"]
                try:
                    function_args = json.loads(response_message["function_call"]["arguments"])
                except json.decoder.JSONDecodeError:
                    function_args = {}
                fuction_to_call = available_functions[function_name]
                function_args['file_dict'] = self.file_dict
                if function_name == 'write_files':
                    function_response, self.file_dict = fuction_to_call(**function_args)
                else:
                    function_response = fuction_to_call(**function_args)
                self.sub_messages.append(response_message)
                self.sub_messages.append(
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    }
                )
            # write_files_from_dict(self.file_dict)
            # self.sub_messages.append({"role": "user", "content": "Write unit tests for the code.", "function_call": {"name": "write_files"}})
            # try:
            #     response_message = self.get_llm_response(self.sub_messages)
            # except InvalidRequestError as e:
            #     if 'maximum context' in e.args[0]:
            #         raise e          
            # if response_message.get("function_call"):
            #     function_name = response_message["function_call"]["name"]
            #     try:
            #         function_args = json.loads(response_message["function_call"]["arguments"])
            #     except json.decoder.JSONDecodeError:
            #         function_args = {}
            #     fuction_to_call = available_functions[function_name]
            #     function_args['file_dict'] = self.file_dict
            #     if function_name == 'write_files':
            #         function_response, self.file_dict = fuction_to_call(**function_args)
            #     else:
            #         function_response = fuction_to_call(**function_args)
            #     self.sub_messages.append(response_message)
            #     self.sub_messages.append(
            #         {
            #             "role": "function",
            #             "name": function_name,
            #             "content": function_response,
            #         }
            #     )
            # write_files_from_dict(self.file_dict)
            self.print_dialog(self.sub_messages)
            write_files_from_dict(self.file_dict, base_dir=f'{self.folder_path}/{self.name}/files')
            self.save_agent_state(self.sub_messages)
            print('')
        except Exception as e:
            print(e)
            print('Error in ZeroShot')
            print('')
            print('Saving state')
            self.save_agent_state(self.sub_messages)
            raise e


