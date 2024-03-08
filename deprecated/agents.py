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
    # elif method_name == "relentless":
    #     agent = RelentlessAgent(env, config, logger, rate_limiter)
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

class HumanAgent(Agent):
    def __init__(self, env, config, logger, rate_limiter):
        super().__init__(env, config, logger, rate_limiter)
        self.name = 'human'

    def run(self, state):
        action = r"""
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

def train_model(X_train, y_train):
    # Identify categorical columns
    categorical_columns = X_train.select_dtypes(include=['category']).columns

    # Apply one-hot encoding to categorical columns and standard scaling to numeric columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), X_train.select_dtypes(exclude=['category']).columns),
            ('cat', OneHotEncoder(), categorical_columns)
        ])

    X_train_processed = preprocessor.fit_transform(X_train)

    model = LogisticRegression()
    model.fit(X_train_processed, y_train)
    return model, preprocessor"""

        # Return the action as a string
        return action
    
class ZeroShotAgent(Agent):
    def __init__(self, env, config, logger, rate_limiter):
        super().__init__(env, config, logger, rate_limiter)
        self.name = 'zero_shot'

    def run(self, state):
        llm_config = self.get_llm_config()
        prompt = self.env.create_baseline_prompt()
#         zero_shot_prompt = f'''
# Objective: Write python code for a data science pipeline task to achieve the highest classification accuracy possible.

# The code written should import all libraries you are to use, and should have the function ```def train_model(X_train: DataFrame, y_train: ndarray) -> Tuple[BaseEstimator, ColumnTransformer]:```.  This function runs the data science pipeline. This involves processing X_train, and returning a tuple of the trained model and a preprocessor used for preprocessing the input features.

# You cannot load or write any external data. You only have access to the data given in the function `train_model`. Only provide the function and library imports, do not include any example code on how to use the function.

# Return code only in ``` backticks.

# The X_train dataframe has the following column names: {state}'''
        llm_config['messages'] = [
                        {"role": "system", "content": "You are an automated expert data scientist. You write code only in Python."},
                        {"role": "user", "content": zero_shot_prompt},
                    ]
        response = chat_completion_rl(**llm_config)
        text = response['choices'][0]['message']['content']
        match = re.search(r'```python\n(.*?)\n```', text, re.DOTALL)
        if match:
            code = match.group(1)
        else:
            match = re.search(r'``` python\n(.*?)\n```', text, re.DOTALL)
            if match:
                code = match.group(1)
            else:
                match = re.search(r'```(.*?)```', text, re.DOTALL)
                if match:
                    code = match.group(1)
                else:
                    code = None
                    raise ValueError(f"Could not find code in response: {text}")
        action = code
        return action
    
STEPS = 'three'

class DSActor:
    def __init__(self,
                get_llm_config_factory,
                root=False,
                state_chat_messages=[],
                system_message='',
                internal_max_steps=3,
                subtask_running_code='',
                env=None,
                ):
        self.root = root
        self.system_message = system_message
        self.state_chat_messages = state_chat_messages
        self.children = []
        self.inbox = []
        self.get_llm_config_factory = get_llm_config_factory
        self.steps = []
        self.internal_max_steps = internal_max_steps
        self.env = env
        self.subtask_running_code = subtask_running_code
    
    def complete_chat(self):
        llm_config = self.get_llm_config_factory()
        llm_config['messages'] = self.state_chat_messages
        response = chat_completion_rl(**llm_config)
        latest_message = dict(response['choices'][0]['message'])
        self.state_chat_messages.append(latest_message)
        return latest_message['content']
    
    def parse_steps_output_into_list(self, string_steps_input):
        llm_config = self.get_llm_config_factory()
        llm_config['messages'] = [{'role': 'system', 'content': 'You are a tool that takes in an input an gives the output in strictly valid JSON such that it can be loaded with python `json.loads`. Only respond with the JSON output.'}, {'role': 'user', 'content': f"""
Please process the following string into a list of {STEPS} string steps, called `steps`, where each value is the string for that step copied exactly including the step number: ```
{string_steps_input}
```"""}]
        response = chat_completion_rl(**llm_config)
        try:
            output = json.loads(response['choices'][0]['message']['content'])
        except Exception as e:
            print(response)
            raise e
        return output['steps']
    
    def run(self, prompt_message, return_bool=False, return_code=False):
        if len(self.state_chat_messages) == 0:
            self.state_chat_messages.append({'role': 'system', 'content': self.system_message})
            self.state_chat_messages.append({'role': 'user', 'content': prompt_message})
        else:
            self.state_chat_messages.append({'role': 'user', 'content': prompt_message})
        message = self.complete_chat()
        if self.root and len(self.state_chat_messages) == 3:
            # Split up step-by-step plan into sub actors
            steps = self.parse_steps_output_into_list(message)
            self.steps = steps
            return None
        if return_bool:
            if 'ACCEPT' in message:
                return True
        elif return_code:
            print(f'[RETURNED CODE MESSAGE] {message}')
            code = get_code_from_message(message)
            if code is None:
                raise ValueError(f'Could not find code in message: {message}')
            else:
                return code
        # Check for any tool use
        # Also have seen 'execute the following code'
        if 'EXECUTE_LINES' in message:
            internal_steps = 0
            while (internal_steps < self.internal_max_steps) and 'EXECUTE_LINES' in message:
                code = get_code_from_message(message)
                if self.subtask_running_code:
                    code = self.subtask_running_code + f'\n{code}'
                try:
                    result = self.env.execute_user_code_lines(code)
                except Exception as e:
                    result = f'{e.args[0]}'
                if len(result.split('\n')) > 200: # 200 lines or more
                    result = '\n'.join(result.split('\n')[-200:])
                result_cleaned = '\n'.join([line for line in result.split('\n') if ('[LightGBM] [Warning]' not in line) and ('[LightGBM] [Info]' not in line)])
                self.state_chat_messages.append({'role': 'user', 'content': f'Code Output: {result_cleaned}'})
                message = self.complete_chat()
                internal_steps += 1
        if return_bool:
            return False
        
        # code = get_code_from_message(message)
        # if code is not None:
        # print(message)
        # print('')
        

        


class DSRelentlessAgent(Agent):
    def __init__(self, env, config, logger, rate_limiter):
        super().__init__(env, config, logger, rate_limiter)
        self.name = 'relentless'

    def run(self, state):
        system_message = f"""
You are tasked with developing the best-performing classification model (f1_score) for a given dataset. You must act autonomously and you will receive no human input at any stage. You have to return as a final output the complete python code for completing this task. You have access to the a temporary python file called `main.py` which all code output is appended to.

You can use the following tools:
1. EXECUTE_LINES: Executes the given python code only and returns the std out to you. You can see variables by printing them.
2. EXECUTE_FULL_CODE: Executes the current python file `main.py` and returns all results back to you.

To use a tool, give the command, followed by the code in backticks, and then stop token of ##. This will then be executed and the result given to you. Only print small outputs, as large outputs will be truncated. Provide the minimal code necessary to achieve the task. When executing code include all library imports and previous code you wish to use, as the code is executed in a new python process without history of the previous commands executed.

You cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model and the output returned to you. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.
"""
        initial_prompt_message=f"""
Objective: Write python code for a data science pipeline task to achieve the highest classification f1 score possible.

You already have access to the following local variables: X_train: DataFrame, y_train: ndarray.

The X_train dataframe has the following column names: {state}

Understand the problem (e.g. imbalanced classes etc), by creating a detailed step-by-step plan. Create only {STEPS} steps. Create additional tests, checks and evaluation metrics on the validation dataset at each step when applicable to help make excellent performing model. You have the standard datascience packages installed, including numpy, pandas==1.5.3, imbalanced-learn, sklearn, scikit-learn==1.3.0, matplotlib, seaborn, scipy, statsmodels, xgboost, lightgbm, catboost, tensorflow, keras, pytorch, and fastai. You can use any of these packages, and any other packages you wish to install.
        """
        task_not_complete = True
        max_sub_actor_iterations = 10
        subtask_running_code = ""
        meta_actor = DSActor(get_llm_config_factory=self.get_llm_config, system_message=system_message, root=True, env=self.env, state_chat_messages=[])
        meta_actor.run(initial_prompt_message)
        subtask_actor_steps = meta_actor.steps
        for subtask_actor_step in subtask_actor_steps:
            sub_actor_iterations = 0
            has_completed = False
            sub_actor = DSActor(get_llm_config_factory=self.get_llm_config, state_chat_messages=deepcopy(meta_actor.state_chat_messages), env=self.env, subtask_running_code=subtask_running_code)
            while (sub_actor_iterations < max_sub_actor_iterations) and not has_completed:
                if sub_actor_iterations == 0:
                    sub_actor.run(prompt_message=f"""
Execute step: {subtask_actor_step} \n\n Condition it on existing code: python```
{subtask_running_code}
```""")
                else:
                    has_completed = sub_actor.run(prompt_message=f"""
Has the task been completed of: ```
{subtask_actor_step}
``` \n\n If yes, return ACCEPT, otherwise reflect and return the full complete corrected code to complete the task, and execute that code by including EXECUTE_LINES in the response. Be sure to include all libraries and define any variables that you use, as the code is executed in a new python subprocess.
""", return_bool=True)
                sub_actor_iterations += 1
            subtask_running_code = sub_actor.run(prompt_message=f'Return the complete concise code with all print statements removed.', return_code=True)
        action_code = meta_actor.run(prompt_message=f"""
Process the existing generated code and return it in the following format.
                                     
Output format: The code written should import all libraries you are to use, and should have the function ```def train_model(X_train: DataFrame, y_train: ndarray) -> Tuple[BaseEstimator, ColumnTransformer]:```.  This function runs the data science pipeline. This involves processing X_train, and returning a tuple of the trained model and a preprocessor used for preprocessing the input features.
                                     
Existing code to process: {subtask_running_code}""", return_code=True)
        return action_code
    


class LLMatic(Agent):
    def __init__(self, env, config, logger, rate_limiter):
        super().__init__(env, config, logger, rate_limiter)
        self.name = 'LLMatic'
        # self.load_from_checkpoint = 'logs/run-20230916-150600_LLMatic_donnemartin|system-design|oop|whatsapp_0_1-runs_log/whatsapp/current_LLMatic_state.json'
        self.load_from_checkpoint = ''

        # self.load_from_checkpoint = 'logs/run-20230915-003040_LLMatic_donnemartin|system-design|oop|parking_lot-donnemartin|system-design|oop|online_chat-donnemartin|system-design|oop|call_center_0_3-runs_log/parking_lot/current_LLMatic_state.json'
        # self.load_from_checkpoint = 'logs/run-20230915-012841_LLMatic_donnemartin|system-design|oop|parking_lot-donnemartin|system-design|oop|online_chat-donnemartin|system-design|oop|call_center_0_3-runs_log/parking_lot/LLMatic_state_beginning_step_5.json'
        # self.load_from_checkpoint = 'logs/run-20230915-012841_LLMatic_donnemartin|system-design|oop|parking_lot-donnemartin|system-design|oop|online_chat-donnemartin|system-design|oop|call_center_0_3-runs_log/parking_lot/LLMatic_state_beginning_step_6.json'
        # self.load_from_checkpoint = 'logs/run-20230916-025445_LLMatic_donnemartin|system-design|oop|parking_lot-donnemartin|system-design|oop|online_chat-donnemartin|system-design|oop|call_center_0_1-runs_log/parking_lot/LLMatic_state_beginning_step_9.json'
        # self.load_from_checkpoint = 'logs/run-20230916-121004_LLMatic_donnemartin|system-design|oop|parking_lot-donnemartin|system-design|oop|online_chat-donnemartin|system-design|oop|call_center_0_1-runs_log/parking_lot/LLMatic_state_beginning_step_6.json'
        # self.load_from_checkpoint = 'logs/run-20230916-112031_LLMatic_donnemartin|system-design|oop|parking_lot-donnemartin|system-design|oop|online_chat-donnemartin|system-design|oop|call_center_0_1-runs_log/parking_lot/LLMatic_state_beginning_step_9.json'
        if self.load_from_checkpoint:
            with open(self.load_from_checkpoint, 'r') as f:
                data = json.load(f)
            self.file_dict = data['file_dict']
            self.steps = data['steps']
            self.step = data['step']
            self.meta_messages = data['meta_messages']
            self.base_dialog = data['base_dialog']
            self.sub_messages = data['sub_messages']

            # # Path for old files
            # self.file_dict['test_all.py'] = self.file_dict['unit_tests.py']
            # del(self.file_dict['unit_tests.py'])
        else:
            self.file_dict = {}
            self.steps = []
            self.step = None
            self.meta_messages = []
            self.base_dialog = []
            self.sub_messages = []
        
        write_files_from_dict(self.file_dict)

        self.folder_path = f"{self.config.run.log_path.split('.txt')[0]}/{self.env.env_task_id}/"
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


Python toolbelt preferences:
- pytest
- dataclasses

Objective:```
{task_description}
```
                            
Understand the problem, by creating a detailed step-by-step plan. Try to solve the problem in the minimal steps necessary. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once. Only create a detailed plan to begin with, which includes designing and running tests to check that they all pass.                              
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
Execute step: {step} \n\n Condition it on existing code files: {list(self.file_dict.keys())}\nPlease now select which files you want to view, and view them.
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
Execute step: {step} \n\n Condition it on existing code: {list(self.file_dict.keys())}\nPlease now select which files you want to view, and view them.
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
``` \n\n If yes, return ACCEPT, otherwise reflect and return the full complete corrected code to complete the task, use the defined functions to write the code.
"""})
                    self.print_dialog(self.sub_messages)
                print('sub step completed')
            print('All steps complete')
            print('')
        except Exception as e:
            print(e)
            print('Error in LLMatic')
            print('')
            print('Saving state')
            self.save_agent_state(self.sub_messages)
            raise e