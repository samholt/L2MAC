import wandb
import random
import numpy as np
import openai
from llm_utils import chat_completion_rl
import re
import json
from copy import deepcopy
from llm_utils import get_llm_config
from llm_utils import setup_chat_rate_limiter, chat_completion_rl, get_llm_config, num_tokens_consumed_by_chat_request, get_model_max_tokens, embedding_rl, pretty_print_chat_messages
from utils.llm_tools import process_function_call_and_return_message, function_definition_list_factory, available_functions_factory, hash_messages, process_functions_into_function_names, clean_string, detect_cycles
from summarizer_and_modifier import add_line_numbers, write_files_from_dict, load_code_files_into_dict
from openai.error import InvalidRequestError
from pathlib import Path
from log_evaluator import count_errors_from_file_dict, run_tests_from_file_dict
import pandas as pd
import traceback
import re

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


def extract_failed_tests(test_output):
    # Search for the failed tests count in the test output string
    match = re.search(r'(\d+) failed', test_output)
    if match:
        # Extract the number of failed tests
        failed_tests_count = int(match.group(1))
    else:
        # Default to 10 if no match is found
        failed_tests_count = 10

    return failed_tests_count

def initialize_agent(method_name, env, config, rate_limiter, wandb_project_name=None, logger=None):
    # Initialize Weights & Biases if a project name is provided
    if wandb_project_name:
        wandb.init(project=wandb_project_name, config=config)

    # Depending on the method name, initialize the agent
    if method_name == "human":
        agent = HumanAgent(env, config, logger, rate_limiter)
    elif method_name == "LLMatic":
        agent = LLMatic(env, config, logger, rate_limiter)
    elif method_name in ["ZeroShot", 'SelfRefine', 'CodeT', 'Reflexion']:
        agent = ZeroShotAgent(env, config, logger, rate_limiter, variant=method_name)
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

class LLMatic(Agent):
    def __init__(self, env, config, logger, rate_limiter):
        super().__init__(env, config, logger, rate_limiter)
        self.name = 'LLMatic'
        self.load_from_checkpoint = ''
        self.replay_llm_responses_path = ''
        self.replay_llm_responses_path_index = 0
        self.responses = []
        self.message_hash_same_increase_temperature = 0
        self.step_idx = 0
        self.max_re_tries = 30
        self.re_tries = 0
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
            self.message_hash = data['message_hash']
        else:
            self.file_dict = {}
            self.steps = []
            self.step = None
            self.meta_messages = []
            self.base_dialog = []
            self.sub_messages = []
            self.responses = []
            self.message_hash = hash_messages([])
        
        write_files_from_dict(self.file_dict)

        self.folder_path = f"{self.config.run.log_path.split('.txt')[0]}/{self.env.env_task_id}/{self.env.seed}/"
        Path(self.folder_path).mkdir(parents=True, exist_ok=True)
        self.max_tokens = get_model_max_tokens(config)
        self.functions = function_definition_list_factory()
        self.system_message = {"role": "system", "content": f'''
Objective: Write code for a large system design task.
Please note that the code should be fully functional. No placeholders.
Only use the functions you have been provided with.
Only use the `write_files` to output code.

You must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task, and correctly incorporate it into the existing code base.
You always write out the whole file contents. You always indent code with tabs.
Please always view the files before writing to them, to make sure you are writing to the correct files.
When writing a test, make the filename start with the prefix 'test_'.

Provide the minimal code necessary to achieve the task conditioned on the existing generated code---including changing the existing generated code.

You cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.

You cannot use any databases as none are setup in the local environment, instead mock a database with an in memory dictionary to store data. No data saved to disk will persist between steps or write operations.
                               
If a test is failing the error could be the code, or the test is incorrect, so feel free to overwrite and change the tests when they are incorrect, to make all tests pass.

Use the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.
'''}

    def print_dialog(self, messages, response_msg=False):
        num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
        pretty_print_chat_messages(messages, num_tokens, self.max_tokens, logger=self.logger, response_msg=response_msg, step_idx=self.step_idx, total_steps=len(self.steps), max_re_tries=self.max_re_tries, re_tries=
self.re_tries)

    def save_agent_state(self, messages, beginning_step=''):
        data_to_save = {'messages': messages,
                        'file_dict': self.file_dict,
                        'steps': self.steps,
                        'step': self.step,
                        'meta_messages': self.meta_messages,
                        'base_dialog': self.base_dialog,
                        'sub_messages': self.sub_messages,
                        'message_hash': self.message_hash,
                        }
        if not beginning_step:
            path = f'{self.folder_path}current_{self.name}_state.json' 
        else:
            path = f'{self.folder_path}LLMatic_state_beginning_step_{self.step_idx}.json'
        with open(path, 'w') as f:
            json.dump(data_to_save, f)

    def get_llm_response(self, messages, max_tokens=None):
        self.print_dialog(messages)
        self.save_agent_state(messages)
        llm_config = self.get_llm_config()
        if max_tokens is not None:
            llm_config['max_tokens'] = max_tokens
        llm_config['messages'] = messages
        # Check if the messages have changed, if they have, then set temperature to zero, if still the same then set temperature to 0.1, as we are repeating ourselves.
        tmp_messages = [clean_string(str(msg)) for msg in messages]
        if detect_cycles(tmp_messages):
            self.message_hash_same_increase_temperature += 0.4
            if self.message_hash_same_increase_temperature >= 1:
                self.message_hash_same_increase_temperature = 1
            self.logger.info(f'[Increasing LLM temperature to {self.message_hash_same_increase_temperature}]')
        else:
            if self.message_hash_same_increase_temperature > 0:
                self.logger.info(f'[Annealing LLM temperature to {self.message_hash_same_increase_temperature}]')
                self.message_hash_same_increase_temperature -= 0.1
                if self.message_hash_same_increase_temperature <= 0:
                    self.message_hash_same_increase_temperature = 0
        llm_config['temperature'] = self.message_hash_same_increase_temperature
        # # message_hash = hash_messages(messages)
        # if message_hash == self.message_hash:
        #     self.message_hash_same_increase_temperature += 0.4
        #     if self.message_hash_same_increase_temperature >= 1:
        #         self.message_hash_same_increase_temperature = 1
        #     llm_config['temperature'] = self.message_hash_same_increase_temperature
        # else:
        #     self.message_hash_same_increase_temperature = 0
        # self.message_hash = message_hash
        llm_config['functions'] = self.functions
        if messages[-1].get('function_call'):
            llm_config['function_call'] = messages[-1]['function_call']
            del(messages[-1]['function_call'])
        if self.replay_llm_responses_path:
            with open(self.replay_llm_responses_path, 'r') as f:
                responses = json.load(f)
            response = responses[self.replay_llm_responses_path_index]
            self.replay_llm_responses_path_index += 1
            if 'error' in response:
                raise InvalidRequestError(response['error'], '')
        else:
            try:
                # Check number of tokens
                num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
                if num_tokens > self.max_tokens:
                    raise InvalidRequestError('InvalidRequestError', 'SelfGeneratedErrorOverTokenLimit')
                response = chat_completion_rl(**llm_config)
                self.responses.append(response)
                with open(f'{self.folder_path}{self.name}_llm_responses.json', 'w') as f:
                    json.dump(self.responses, f)
            except openai.error.InvalidRequestError as e:
                self.responses.append({'error': 'InvalidRequestError'})
                self.logger.error('Error: InvalidRequestError')
                self.logger.error(traceback.format_exc())
                self.logger.info("Error:", e.__dict__)  # or use a logging framework
                raise e
        message_response = response["choices"][0]["message"]
        if not message_response.get('content'):
            message_response['content'] = None
        self.print_dialog([message_response], response_msg=True)
        return message_response

    def get_function_names_as_str(self):
        fns = process_functions_into_function_names(self.functions)
        return ', '.join([f'`{fn}`'for fn in fns])

    def run(self, state=''):
        try:
            return self._run(state)
        except Exception as e:
            self.logger.error('Error in LLMatic.run()')
            self.logger.error(e)
            self.logger.error(traceback.format_exc())
            self.save_agent_state(self.sub_messages)
            write_files_from_dict(self.file_dict, base_dir=f'{self.folder_path}/{self.name}')
            raise e


    def _run(self, state=''):
        if not self.load_from_checkpoint:
            # unit_tests = self.env.ut
            # self.file_dict['test_all.py'] = add_line_numbers(unit_tests.split('\n'))
            self.meta_messages = [self.system_message]
            task_description = self.env.desc
            # Read the unit tests from the environment
            # with open(f'./data/donnemartin-system-design-oop/object_oriented_design/{self.env.env_task_id}/unit_tests_train.py', 'r') as f:
            #     unit_tests = f.read()
            self.meta_messages.append({"role": "user", "content": f"""
You will get instructions for code to write.
First lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.
Do not comment on what every file does. Please note that the code should be fully functional. No placeholders.

You will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.
Please note that the code should be fully functional. No placeholders.

Follow a language and framework appropriate best practice file naming convention.
Make sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.
When writing code if you are unsure, write a plausible implementation.
Include module dependency or package manager dependency definition file.

Useful to know:

For Python, you always create an appropriate requirements.txt file.
Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.
You can use any package and any other packages you wish to install.
You cannot use any databases as none are setup in the local environment, instead mock a database with an in memory dictionary to store data. No data saved to disk will persis between steps or write operations.
When writing a test, make the filename start with the prefix 'test_'.
                                       
Python toolbelt preferences:
- pytest
- dataclasses
- flask

Objective:```
{task_description}
```

Understand the problem, by creating an extremely detailed step-by-step plan, where each step is long (multiple sentences) and in total includes every single feature requirement specified above, feel free to copy directly from it. Use no more than 10 steps in the plan. Create additional tests, checks and evaluation at each step when applicable to help make an excellent code implementation, where all the code is fully functional. Use best software design practices, and you can output large amounts of code at once. Please include a last sentence to create and run tests when implementing or writing code in that same step. You will receive no human input at any stage, so you cannot use a human to test. Only create a detailed plan to begin with, which includes designing and running tests to check that they all pass. Please be sure to include all of the specified feature requirements in the following plan.
""", "function_call": {"name": "provide_detailed_sub_task_steps_for_sub_agents"}})
        steps = []
        # Loop until we get a multi-step plan, as sometimes the first plan is not multi-step, and only a single step.
        max_reflections = 1
        current_reflection = 0
        current_dialog = deepcopy(self.meta_messages)
        if 'insight-large-code-base' in self.env.env_name:
            self.file_dict = load_code_files_into_dict(self.env.code_path, file_extensions=['.py'])
            print('')
        while len(steps) <= 50 and current_reflection < max_reflections:
            current_reflection += 1
            initial_response_message = self.get_llm_response(current_dialog)
            current_dialog.append(initial_response_message)
            current_dialog.append({"role": "user", "content": f"""
Please reflect on the plan, and increase the number of generated steps to that of 100 or so very detailed steps that include all the feature requirements.
"""})
            # Could reflect and improve plan etc a few times here.
            function_name = initial_response_message["function_call"]["name"]
            try:
                function_args = json.loads(initial_response_message["function_call"]["arguments"])
            except json.decoder.JSONDecodeError:
                try:
                    function_args = json.loads(initial_response_message["function_call"]["arguments"].replace('\n', ''))
                except json.decoder.JSONDecodeError:
                    try:
                        function_args = json.loads(initial_response_message["function_call"]["arguments"] + '"]}')
                    except json.decoder.JSONDecodeError:
                        try:
                            function_args = json.loads(initial_response_message["function_call"]["arguments"] + '"]}')
                        except json.decoder.JSONDecodeError:
                            try:
                                function_args = json.loads(initial_response_message["function_call"]["arguments"] + ']}')
                            except Exception as e:
                                print(e)
            fuction_to_call = available_functions_factory()[function_name]
            steps = fuction_to_call(**function_args)
        self.steps = steps
        # self.base_dialog = deepcopy(current_dialog)
        self.base_dialog = deepcopy([self.system_message])
        # Remove provide_detailed_sub_task_steps_for_sub_agents function from functions list
        self.functions = [function for function in self.functions if function['name'] != 'provide_detailed_sub_task_steps_for_sub_agents']
        previous_step_output_summary = ""
        # errors_df_l = []
        # count_change_times = 0
        # method = 'llmatic'
        for step_idx, step in enumerate(self.steps):
            step = step
            self.step = deepcopy(step)
            self.step_idx = step_idx
            self.sub_messages = deepcopy(self.base_dialog)
            self.save_agent_state(self.sub_messages, beginning_step=self.step)
            self.sub_messages.append({"role": "user", "content": f"""
Objective: Execute sub task step: {step}.\n\n Note: Condition any new code files on the existing code files: {list(self.file_dict.keys())}. Fully implement these features in the code, no placeholders. You can now optionally view the existing files if you need to view them to complete the current task step. You have a limited context window so be selective about which files you view, only view the files you think you might need to view.\n\nSummary output of previous step: ""{previous_step_output_summary}""\n\nRespond now only with a function call of one of the following functions provided: {self.get_function_names_as_str()}, and if you want to output code only use the `write_files` function to output code.
"""})
            has_completed_sub_step = False
            task_step_complete = False
            self.max_re_tries = 30
            self.re_tries = 0
            while not has_completed_sub_step:
                try:
                    response_message = self.get_llm_response(self.sub_messages)
                    if task_step_complete:
                        previous_step_output_summary = response_message['content']
                        has_completed_sub_step = True
                        break
                except InvalidRequestError as e:
                    # Calculate exactly where the token limit overflowed, and undo messages till just before it overflowed.
                    while (self.max_tokens - num_tokens_consumed_by_chat_request(messages=self.sub_messages, functions=self.functions)) < 700:
                        # self.sub_messages = self.sub_messages[:-1]
                        self.sub_messages.pop(3)
                    self.sub_messages.append({"role": "user", "content": f"""
You have exhausted your context window. Reflect on your progress. Provide a short concise response, of two sentences maximum, this will be used to restart this step from the beginning without the previous messages.""", "function_call": 'none'})
#                     self.sub_messages.append({"role": "user", "content": f"""
# You have exhausted your context window. Please state only which files are necessary to view to complete this task, i.e. those files which the newly written files import from. Also reflect on your progress. Provide a short concise response, of two sentences maximum, this will be used to restart this step from the beginning without the previous messages.""", "function_call": 'none'})
                    response_message = self.get_llm_response(self.sub_messages)
                    summary_step_message = response_message['content']
                    # if 'maximum context' in e.args[0]:
                    self.re_tries += 1
                    if self.re_tries > self.max_re_tries:
                        # raise e
                        has_completed_sub_step = True
                        self.logger.warning(f'[WARNING] Maximum re-tries reached: {self.re_tries}/{self.max_re_tries}, skipping step')
                        # break
                        raise ValueError(f'[ERROR] Maximum re-tries reached: {self.re_tries}/{self.max_re_tries}, stopping run.')
                    # Restart the step. Should control re-try times.
                    self.sub_messages = deepcopy(self.base_dialog)
                    # Following is 63 tokens
                    self.sub_messages.append({"role": "user", "content": f"""
Objective: Execute sub task step: {step} \n\n Note: Condition any new code files on the existing code files: {list(self.file_dict.keys())} Fully implement these features in the code, no placeholders. You can now optionally view the existing files if you need to view them to complete the current task step. You have a limited context window so be selective about which files you view, only view the files you think you might need to view. \n\n {summary_step_message}\n\nRespond now only with a function call of one of the following functions provided: {self.get_function_names_as_str()}, and if you want to output code only use the `write_files` function to output code.
"""})
                    response_message = self.get_llm_response(self.sub_messages)
                self.sub_messages.append(response_message)
                if response_message.get("function_call"):
                    function_return_message, self.file_dict = process_function_call_and_return_message(response_message["function_call"], self.file_dict, functions=self.functions)
                    if 'status' in json.loads(function_return_message['content']) and json.loads(function_return_message['content'])['status'] == 'TASK_STEP_COMPLETE':
                        task_step_complete = True
                        self.sub_messages.append({"role": "user", "content": f"""
Please provide a one or two sentence summary of the output of this step, which is useful for the next step. Your response will be used when starting the next step without any of the previous messages.""", "function_call": 'none'})
                        continue
                    self.sub_messages.append(function_return_message)
                    if 'name' in function_return_message and function_return_message['name'] == 'sub_task_step_complete' and json.loads(function_return_message['content'])['status'] == 'error':
                        self.sub_messages.append({"role": "user", "content": f"""
{json.loads(function_return_message['content'])['message']}

Reflect and write the full complete corrected code to correct the code. Only use the functions you have been provided with, and if you want to output code only use the `write_files` function to output code. Condition it on existing code: {list(self.file_dict.keys())}\nRespond now only with a function call of one of the following functions provided: {self.get_function_names_as_str()}, and if you want to output code only use the `write_files` function to output code.
"""})
                    else:        
                        self.sub_messages.append({"role": "user", "content": f"""
Has the sub task step been completed of: ```
{step}
``` \n\n If yes, call the function `sub_task_step_complete`, otherwise reflect and correct the full code to complete the task. Only use the functions you have been provided with, and if you want to output code only use the `write_files` function to output code. Condition it on existing code: {list(self.file_dict.keys())} Fully implement these features in the code, no placeholders. If you have not viewed the files before writing to them, please view them, to make sure you are writing to the correct files.\nRespond now only with a function call of one of the following functions provided: {self.get_function_names_as_str()}, and if you want to output code only use the `write_files` function to output code.
"""})
                else:
                    self.sub_messages.append({"role": "user", "content": f"""
Has the sub task step been completed of: ```
{step}
``` \n\n If yes, call the function `sub_task_step_complete`, otherwise reflect and correct the full code to complete the task. Only use the functions you have been provided with, and if you want to output code only use the `write_files` function to output code. Condition it on existing code: {list(self.file_dict.keys())} Fully implement these features in the code, no placeholders. If you have not viewed the files before writing to them, please view them, to make sure you are writing to the correct files.\nRespond now only with a function call of one of the following functions provided: {self.get_function_names_as_str()}, and if you want to output code only use the `write_files` function to output code.
"""})
                write_files_from_dict(self.file_dict)
            self.logger.info('[STEP COMPLETE] sub step completed')
        self.logger.info('[TASK COMPLETE SUCCESSFULLY!!] All steps complete')
        self.logger.info('')
        write_files_from_dict(self.file_dict, base_dir=f'{self.folder_path}/{self.name}')
        self.save_agent_state(self.sub_messages)
        return f'{self.folder_path}/{self.name}'

    
class ZeroShotAgent(Agent):
    def __init__(self, env, config, logger, rate_limiter, variant='ZeroShot'):
        super().__init__(env, config, logger, rate_limiter)
        self.name = variant
        self.load_from_checkpoint = ''
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
        self.functions = function_definition_list_factory()
        self.system_message = {"role": "system", "content": f'''
Objective: Write code for a large system design task.
Please note that the code should be fully functional. No placeholders.
Only use the functions you have been provided with.
Only use the `write_files` to output code.

You must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task, and correctly incorporate it into the existing code base.
You always write out the whole file contents. You always indent code with tabs.
Please always view the files before writing to them, to make sure you are writing to the correct files.
When writing a test, make the filename start with the prefix 'test_'.

Provide the minimal code necessary to achieve the task conditioned on the existing generated code---including changing the existing generated code.

You cannot visualize any graphical output.

You cannot use any databases as none are setup in the local environment, instead mock a database with an in memory dictionary to store data. No data saved to disk will persist between steps or write operations.

Python toolbelt preferences:
- pytest
- dataclasses
- flask
                               
When writing code, do not make a single file long, instead split it into multiple files, such that each file can be separately tested.

Never use any time.sleep inside tests, instead if you want to use the passage of time in a test mock it only. All tests written should be fast to run and verify.
Use the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.
'''}

    def print_dialog(self, messages):
        num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
        pretty_print_chat_messages(messages, num_tokens, self.max_tokens, logger=self.logger)

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
            path = f'{self.folder_path}current_{self.name}_state.json' 
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
            if 'error' in response:
                raise InvalidRequestError(response['error'], '')
        else:
            try:
                # Check number of tokens
                num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
                if num_tokens > self.max_tokens:
                    raise InvalidRequestError('InvalidRequestError', 'SelfGeneratedErrorOverTokenLimit')
                response = chat_completion_rl(**llm_config)
                self.responses.append(response)
                with open(f'{self.folder_path}{self.name}_llm_responses.json', 'w') as f:
                    json.dump(self.responses, f)
            except openai.error.InvalidRequestError as e:
                self.responses.append({'error': 'InvalidRequestError'})
                self.logger.error('Error: InvalidRequestError')
                self.logger.error(traceback.format_exc())
                self.logger.info("Error:", e.__dict__)  # or use a logging framework
                raise e
        message_response = response["choices"][0]["message"]
        if not message_response.get('content'):
            message_response['content'] = None
        return message_response

    def get_function_names_as_str(self):
        fns = process_functions_into_function_names(self.functions)
        return ', '.join([f'`{fn}`'for fn in fns])

    def run(self, state=''):
        try:
            return self._run(state)
        except Exception as e:
            self.logger.error(f'Error in {self.name}.run()')
            self.logger.error(e)
            self.logger.error(traceback.format_exc())
            self.save_agent_state(self.sub_messages)
            write_files_from_dict(self.file_dict, base_dir=f'{self.folder_path}/{self.name}')
            raise e

    def _run(self, state=''):
        self.meta_messages = [self.system_message]
        task_description = self.env.desc
        # with open(f'./data/donnemartin-system-design-oop/object_oriented_design/{self.env.env_task_id}/unit_tests_train.py', 'r') as f:
        #     unit_tests = f.read()
        self.meta_messages.append({"role": "user", "content": f"""
You will get instructions for code to write.
First lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.
Do not comment on what every file does. Please note that the code should be fully functional. No placeholders.

You will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.
Please note that the code should be fully functional. No placeholders.

Follow a language and framework appropriate best practice file naming convention.
Make sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.
When writing code if you are unsure, write a plausible implementation.
Include module dependency or package manager dependency definition file.

Useful to know:

Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.
You can use any package and any other packages you wish to install.
You cannot use any databases as none are setup in the local environment, instead mock a database with an in memory dictionary to store data. No data saved to disk will persis between steps or write operations.
When writing a test, make the filename start with the prefix 'test_'.
                                       
Python toolbelt preferences:
- pytest
- dataclasses
- flask

Objective:```
{task_description}
```

Only output all code now, which includes writing tests. Make this a long response. Create additional tests for the generated code, and make sure all the code generated is fully functional.
""", "function_call": {"name": "write_files"}})
        # Remove provide_detailed_sub_task_steps_for_sub_agents function from functions list
        self.functions = [function for function in self.functions if function['name'] != 'provide_detailed_sub_task_steps_for_sub_agents']
        task_step_complete = False
        if self.name == 'ZeroShot':
            response_message = self.get_llm_response(self.meta_messages)
            self.sub_messages.append(response_message)
            if response_message.get("function_call"):
                function_return_message, self.file_dict = process_function_call_and_return_message(response_message["function_call"], self.file_dict)
                self.sub_messages.append(function_return_message)
                task_step_complete = True
        elif self.name == 'SelfRefine':
            response_message = self.get_llm_response(self.meta_messages)
            self.sub_messages.append(response_message)
            if response_message.get("function_call"):
                function_return_message, self.file_dict = process_function_call_and_return_message(response_message["function_call"], self.file_dict)
                self.sub_messages.append(function_return_message)
                iterations = 0
                while not task_step_complete:
                    iterations += 1
                    self.sub_messages.append({"role": "user", "content": f"""
Using the generated code. Can you give one suggestion to improve it to the original given task. Don't fix the code, just give a suggestion.
""", "function_call": "none"})
                    try:
                        response_message = self.get_llm_response(self.sub_messages)
                        self.sub_messages.append(response_message)
                    except InvalidRequestError as e:
                        break
                    self.sub_messages.append({"role": "user", "content": f"""
Now fix the code.\n\nRespond now only with a function call of one of the following functions provided: {self.get_function_names_as_str()}, and if you want to output code only use the `write_files` function to output code.
"""})
                    try:
                        response_message = self.get_llm_response(self.sub_messages)
                        self.sub_messages.append(response_message)
                        if response_message.get("function_call"):
                            function_return_message, self.file_dict = process_function_call_and_return_message(response_message["function_call"], self.file_dict, functions=self.functions)
                            self.sub_messages.append(function_return_message)
                            self.logger.info(f'[Baseline {self.name} | Iteration {iterations}]')
                            if iterations >= 3:
                                break
                            if 'status' in json.loads(function_return_message['content']) and json.loads(function_return_message['content'])['status'] == 'TASK_STEP_COMPLETE':
                                task_step_complete = True
                                break
                    except InvalidRequestError as e:
                        break
        elif self.name == 'CodeT':
            file_dicts = []
            for i in range(3):
                self.meta_messages[-1]['function_call'] = {"name": "write_files"}
                response_message = self.get_llm_response(self.meta_messages)
                # self.sub_messages.append(response_message)
                if response_message.get("function_call"):
                    function_return_message, file_dict = process_function_call_and_return_message(response_message["function_call"], self.file_dict)
                    if json.loads(function_return_message['content'])['message'] == 'All tests passed.':
                        failures = 0
                    else:
                        failures = extract_failed_tests(json.loads(function_return_message['content'])['message'])
                    file_dicts.append((failures, file_dict))
            file_dicts = sorted(file_dicts, key=lambda x: x[0])
            self.file_dict = file_dicts[0][1]
        elif self.name == 'Reflexion':
            response_message = self.get_llm_response(self.meta_messages)
            self.sub_messages.append(response_message)
            if response_message.get("function_call"):
                function_return_message, self.file_dict = process_function_call_and_return_message(response_message["function_call"], self.file_dict)
                self.sub_messages.append(function_return_message)
                iterations = 0
                reflections = []
                while not task_step_complete:
                    iterations += 1
                    self.sub_messages.append({"role": "user", "content": f"""
Evaluate how many of the original features specified are implemented in the generated code. Please give a scalar value.
""", "function_call": "none"})
                    try:
                        response_message = self.get_llm_response(self.sub_messages)
                        self.sub_messages.append(response_message)
                    except InvalidRequestError as e:
                        break
                    self.sub_messages.append({"role": "user", "content": f"""
You are an advanced reasoning agent that can improve based on self refection. 
Use the previous generated code and the evaluation metric and in a few sentences, Diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.                                                
You will be given a previous reasoning trial in which you were given access to relevant context and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, Diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.

Reflection:""", "function_call": "none"})
                    try:
                        reflection_response_message = self.get_llm_response(self.sub_messages)
                        reflections = [reflection_response_message['content']]
                        # reflections.append(reflection_response_message['content'])
                        self.sub_messages.append(response_message)
                    except InvalidRequestError as e:
                        break
                    reflections_string = '\n'.join(reflections)
                    self.sub_messages = [self.system_message, {"role": "user", "content": f"""
You will get instructions for code to write.
First lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.
Do not comment on what every file does. Please note that the code should be fully functional. No placeholders.

You will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.
Please note that the code should be fully functional. No placeholders.

Follow a language and framework appropriate best practice file naming convention.
Make sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.
When writing code if you are unsure, write a plausible implementation.
Include module dependency or package manager dependency definition file.

Useful to know:

Always add a comment briefly describing the purpose of the function definition.
Add comments explaining very complex bits of logic.
Always follow the best practices for the requested languages for folder/file structure and how to package the project.
You can use any package and any other packages you wish to install.
You cannot use any databases as none are setup in the local environment, instead mock a database with an in memory dictionary to store data. No data saved to disk will persis between steps or write operations.
When writing a test, make the filename start with the prefix 'test_'.
                                       
Python toolbelt preferences:
- pytest
- dataclasses
- flask

Objective:```
{task_description}
```

{reflections_string}

Only output all code now, which includes writing tests. Make this a long response. Create additional tests for the generated code, and make sure all the code generated is fully functional.
""", "function_call": {"name": "write_files"}}]
                    try:
                        response_message = self.get_llm_response(self.sub_messages)
                        self.sub_messages.append(response_message)
                        if response_message.get("function_call"):
                            function_return_message, self.file_dict = process_function_call_and_return_message(response_message["function_call"], {}, functions=self.functions)
                            self.sub_messages.append(function_return_message)
                            self.logger.info(f'[Baseline {self.name} | Iteration {iterations}]')
                            if iterations >= 3:
                                break
                            if 'status' in json.loads(function_return_message['content']) and json.loads(function_return_message['content'])['status'] == 'TASK_STEP_COMPLETE':
                                task_step_complete = True
                                break
                    except InvalidRequestError as e:
                        break







#         # initial_response_message = self.get_llm_response(self.meta_messages)
#         response_message = self.get_llm_response(self.meta_messages)
#         # self.sub_messages = deepcopy(self.meta_messages)
#         # self.sub_messages.append(initial_response_message)
# #         self.sub_messages.append({"role": "user", "content": f"""
# # Now respond with all the code for the task in one response.
# # """, "function_call": {"name": "write_files"}})
#         # try:
#         #     response_message = self.get_llm_response(self.sub_messages)
#         # except InvalidRequestError as e:
#         #     if 'maximum context' in e.args[0]:
#         #         raise e          
#         self.sub_messages.append(response_message)
#         if response_message.get("function_call"):
#             function_return_message, self.file_dict = process_function_call_and_return_message(response_message["function_call"], self.file_dict)
#             self.sub_messages.append(function_return_message)
#         # write_files_from_dict(self.file_dict)
#         # self.sub_messages.append({"role": "user", "content": "Write unit tests for the code.", "function_call": {"name": "write_files"}})
#         # try:
#         #     response_message = self.get_llm_response(self.sub_messages)
#         # except InvalidRequestError as e:
#         #     if 'maximum context' in e.args[0]:
#         #         raise e          
#         # if response_message.get("function_call"):
#         #     function_name = response_message["function_call"]["name"]
#         #     try:
#         #         function_args = json.loads(response_message["function_call"]["arguments"])
#         #     except json.decoder.JSONDecodeError:
#         #         function_args = {}
#         #     fuction_to_call = available_functions[function_name]
#         #     function_args['file_dict'] = self.file_dict
#         #     if function_name == 'write_files':
#         #         function_response, self.file_dict = fuction_to_call(**function_args)
#         #     else:
#         #         function_response = fuction_to_call(**function_args)
#         #     self.sub_messages.append(response_message)
#         #     self.sub_messages.append(
#         #         {
#         #             "role": "function",
#         #             "name": function_name,
#         #             "content": function_response,
#         #         }
#         #     )
#         # write_files_from_dict(self.file_dict)


        # Finish state
        self.logger.info(f'[Baseline {self.name} TASK COMPLETE SUCCESSFULLY!!] All steps complete')
        self.print_dialog(self.sub_messages)
        write_files_from_dict(self.file_dict, base_dir=f'{self.folder_path}/{self.name}')
        self.save_agent_state(self.sub_messages)
        return f'{self.folder_path}/{self.name}'

