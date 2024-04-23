import json
import random
import traceback
from copy import deepcopy
from pathlib import Path
from typing import Optional

import numpy as np
import openai
from openai import APIError

from l2mac.config import L2MACConfig
from l2mac.envs.general import Environment
from l2mac.llm_providers.general import (
    chat_completion_rl,
    get_llm_config,
    get_model_max_tokens,
)
from l2mac.llm_providers.openai import num_tokens_consumed_by_chat_request
from l2mac.llm_providers.rate_limiter import ChatRateLimiter
from l2mac.llm_providers.utils import pretty_print_chat_messages
from l2mac.prompts.load_prompts import L2MACPrompts
from l2mac.tools.core import (
    available_functions_factory,
    function_definition_list_factory,
    process_function_call_and_return_message,
    process_functions_into_function_names,
)
from l2mac.tools.utils import write_files_from_dict
from l2mac.utils.l2mac import clean_string, detect_cycles, hash_messages
from l2mac.utils.run import DebuggingLevel


class L2MAC:
    def __init__(
        self,
        prompt_task: str,
        env: Environment,
        config: L2MACConfig,
        logger: object,
        rate_limiter: ChatRateLimiter,
        l2mac_prompts: L2MACPrompts,
        run_tests: bool = True,
        project_name: Optional[str] = None,
        steps: int = 10,
        prompt_program: Optional[str] = None,
        prompts_file_path: Optional[str] = None,
        tools_enabled: Optional[str] = None,
        debugging_level: DebuggingLevel = DebuggingLevel.info,
        wandb: Optional[object] = None,
    ):
        self.env = env
        self.prompt_task = prompt_task
        self.config = config
        self.seed_value = None
        self.logger = logger
        self.rate_limiter = rate_limiter
        self.l2mac_prompts = l2mac_prompts
        self.name = "L2MAC"
        self.run_tests = run_tests
        self.project_name = project_name
        self.steps = steps
        self.prompt_program = prompt_program
        self.prompts_file_path = prompts_file_path
        self.tools_enabled = tools_enabled
        self.debugging_level = debugging_level
        self.wandb = wandb
        # Internal state
        self.file_dict = {}
        self.step = None
        self.meta_messages = []
        self.base_dialog = []
        self.sub_messages = []
        self.responses = []
        self.message_hash = hash_messages([])
        self.reset()

    def seed(self, seed_value):
        self.seed_value = seed_value
        random.seed(seed_value)
        np.random.seed(seed_value)

    def get_llm_config(self):
        return get_llm_config(self.config, self.logger, self.name, self.rate_limiter)

    def reset(self):
        self.load_from_checkpoint = ""
        self.replay_llm_responses_path = ""
        self.replay_llm_responses_path_index = 0
        self.responses = []
        self.message_hash_same_increase_temperature = 0
        self.step_idx = 0
        self.max_re_tries = 30
        self.re_tries = 0
        if self.load_from_checkpoint:
            with open(self.load_from_checkpoint, "r") as f:
                data = json.load(f)
            self.file_dict = data["file_dict"]
            self.prompt_program = data["prompt_program"]
            self.steps = data["steps"]
            self.step = data["step"]
            self.meta_messages = data["meta_messages"]
            self.base_dialog = data["base_dialog"]
            self.sub_messages = data["sub_messages"]
            self.responses = data["responses"]
            self.message_hash = data["message_hash"]

        self.log_folder_path = f"{self.config.setup.log_path.split('.txt')[0]}_{self.env.env_name}_{self.env.seed}/"
        self.folder_path = f"workspace/{self.project_name + '_' if self.project_name else ''}{self.config.setup.log_path.split('_')[0].split('/')[1]}/"
        Path(self.folder_path).mkdir(parents=True, exist_ok=True)
        Path(self.log_folder_path).mkdir(parents=True, exist_ok=True)
        write_files_from_dict(self.file_dict, base_dir=f"{self.folder_path}")
        self.max_tokens = get_model_max_tokens(self.config)
        self.functions = function_definition_list_factory()
        if self.tools_enabled is not None:
            self.functions = [
                tool for tool in self.functions if tool["function"]["name"] in self.tools_enabled.split(",")
            ]
        system_message = self.l2mac_prompts.system
        self.system_message = {"role": "system", "content": system_message}

    def print_dialog(self, messages, response_msg=False):
        num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
        pretty_print_chat_messages(
            messages,
            num_tokens,
            self.max_tokens,
            logger=self.logger,
            response_msg=response_msg,
            step_idx=self.step_idx,
            total_steps=0 if self.prompt_program is None else len(self.prompt_program),
            max_re_tries=self.max_re_tries,
            re_tries=self.re_tries,
        )

    def save_agent_state(self, messages, beginning_step=""):
        data_to_save = {
            "messages": messages,
            "file_dict": self.file_dict,
            "steps": self.steps,
            "step": self.step,
            "meta_messages": self.meta_messages,
            "base_dialog": self.base_dialog,
            "sub_messages": self.sub_messages,
            "message_hash": self.message_hash,
        }
        if not beginning_step:
            path = f"{self.log_folder_path}current_{self.name}_state.json"
        else:
            path = f"{self.log_folder_path}L2MAC_state_beginning_step_{self.step_idx}.json"
        with open(path, "w") as f:
            json.dump(data_to_save, f)

    def get_llm_response(self, messages, max_tokens=None, tool_choice="auto"):
        self.print_dialog(messages)
        self.save_agent_state(messages)
        llm_config = self.get_llm_config()
        if max_tokens is not None:
            llm_config["max_tokens"] = max_tokens
        llm_config["messages"] = messages
        # Check if the messages have changed, if they have, then set temperature to zero, if still the same then set temperature to 0.1, as we are repeating ourselves.
        tmp_messages = [clean_string(str(msg)) for msg in messages]
        if detect_cycles(tmp_messages):
            self.message_hash_same_increase_temperature += 0.4
            if self.message_hash_same_increase_temperature >= 1:
                self.message_hash_same_increase_temperature = 1
            self.logger.info(f"[Increasing LLM temperature to {self.message_hash_same_increase_temperature}]")
        else:
            if self.message_hash_same_increase_temperature > 0:
                self.logger.info(f"[Annealing LLM temperature to {self.message_hash_same_increase_temperature}]")
                self.message_hash_same_increase_temperature -= 0.1
                if self.message_hash_same_increase_temperature <= 0:
                    self.message_hash_same_increase_temperature = 0
        llm_config["temperature"] = self.message_hash_same_increase_temperature
        llm_config["tools"] = self.functions
        if tool_choice == "auto":
            llm_config["tool_choice"] = "auto"
        elif tool_choice is not None:
            llm_config["tool_choice"] = {"type": "function", "function": {"name": tool_choice}}
        else:
            llm_config["tool_choice"] = "none"
        if self.replay_llm_responses_path:
            with open(self.replay_llm_responses_path, "r") as f:
                responses = json.load(f)
            response = responses[self.replay_llm_responses_path_index]
            self.replay_llm_responses_path_index += 1
            if "error" in response:
                raise APIError(response["error"], "")
        else:
            try:
                # Check number of tokens
                num_tokens = num_tokens_consumed_by_chat_request(messages=messages, functions=self.functions)
                if num_tokens > self.max_tokens:
                    raise APIError("InvalidRequestError", "SelfGeneratedErrorOverTokenLimit")
                response = chat_completion_rl(**llm_config)
                self.responses.append(response)
                with open(f"{self.log_folder_path}{self.name}_llm_responses.json", "w") as f:
                    json.dump(self.responses, f)
            except APIError as e:
                self.responses.append({"error": "InvalidRequestError"})
                self.logger.error("Error: InvalidRequestError")
                self.logger.error(traceback.format_exc())
                self.logger.info("Error:", e.__dict__)  # or use a logging framework
                raise e
        message_response = response["choices"][0]["message"]
        self.print_dialog([message_response], response_msg=True)
        return message_response

    def get_function_names_as_str(self):
        fns = process_functions_into_function_names(self.functions)
        return ", ".join([f"`{fn}`" for fn in fns])

    def get_file_names(self):
        # Simple implementation, for now, can be improved.
        return list(self.file_dict.keys())

    def run(self, steps: int = 10):
        return self._run(steps=steps)

    def _run(self, steps: int = 10):
        self.reset()
        if not self.load_from_checkpoint:
            self.meta_messages = [self.system_message]
            first_message = self.l2mac_prompts.first_message.format(prompt_task=self.prompt_task, steps=steps)
        self.meta_messages.append({"role": "user", "content": first_message})
        prompt_program = []
        # Loop until we get a multi-step plan, as sometimes the first plan is not multi-step, and only a single step.
        max_reflections = 1
        current_reflection = 0
        current_dialog = deepcopy(self.meta_messages)
        if self.prompt_program is None:
            # Bootstrap and generate the prompt program to follow internally to complete the user input prompt task.
            while len(prompt_program) <= 50 and current_reflection < max_reflections:
                current_reflection += 1
                initial_response_message = self.get_llm_response(
                    current_dialog, tool_choice="provide_detailed_sub_task_steps_for_sub_agents"
                )
                current_dialog.append(initial_response_message)
                current_dialog.append(
                    {
                        "role": "user",
                        "content": self.l2mac_prompts.reflect_on_prompt_program,
                    }
                )
                # Could reflect and improve plan etc a few times here.
                function_response = initial_response_message["tool_calls"][0]["function"]
                function_name = function_response["name"]
                try:
                    function_args = json.loads(function_response["arguments"])
                except json.decoder.JSONDecodeError:
                    try:
                        function_args = json.loads(function_response["arguments"].replace("\n", ""))
                    except json.decoder.JSONDecodeError:
                        try:
                            function_args = json.loads(function_response["arguments"] + '"]}')
                        except json.decoder.JSONDecodeError:
                            try:
                                function_args = json.loads(function_response["arguments"] + '"]}')
                            except json.decoder.JSONDecodeError:
                                try:
                                    function_args = json.loads(function_response["arguments"] + "]}")
                                except Exception as e:
                                    print(e)
                fuction_to_call = available_functions_factory()[function_name]
                prompt_program = fuction_to_call(**function_args)
            self.prompt_program = prompt_program
        # self.base_dialog = deepcopy(current_dialog)
        self.base_dialog = deepcopy([self.system_message, {"role": "user", "content": first_message}])
        # Remove provide_detailed_sub_task_steps_for_sub_agents function from functions list
        self.functions = [
            tool
            for tool in self.functions
            if tool["function"]["name"] != "provide_detailed_sub_task_steps_for_sub_agents"
        ]
        previous_step_output_summary = ""
        for step_idx, step in enumerate(self.prompt_program):
            self.step = deepcopy(step)
            self.step_idx = step_idx
            self.sub_messages = deepcopy(self.base_dialog)
            self.save_agent_state(self.sub_messages, beginning_step=self.step)
            self.sub_messages.append(
                {
                    "role": "user",
                    "content": self.l2mac_prompts.control_unit_execute_instruction.format(
                        step=step,
                        file_names=self.get_file_names(),
                        test_writing_advice=self.l2mac_prompts.test_writing_advice,
                        previous_step_output_summary=previous_step_output_summary,
                        functions_provided=self.get_function_names_as_str(),
                    ),
                }
            )
            has_completed_sub_step = False
            task_step_complete = False
            self.max_re_tries = 30
            self.re_tries = 0
            while not has_completed_sub_step:
                try:
                    response_message = self.get_llm_response(self.sub_messages)
                    if task_step_complete:
                        previous_step_output_summary = response_message["content"]
                        has_completed_sub_step = True
                        break
                except openai.BadRequestError:
                    # Calculate exactly where the token limit overflowed, and undo messages till just before it overflowed.
                    while (
                        self.max_tokens
                        - num_tokens_consumed_by_chat_request(messages=self.sub_messages, functions=self.functions)
                    ) < 700:
                        self.sub_messages.pop(3)
                    self.sub_messages.append(
                        {
                            "role": "user",
                            "content": self.l2mac_prompts.control_unit_exhaust_context_window,
                        }
                    )
                    response_message = self.get_llm_response(self.sub_messages, tool_choice=None)
                    summary_step_message = response_message["content"]
                    self.re_tries += 1
                    if self.re_tries > self.max_re_tries:
                        has_completed_sub_step = True
                        self.logger.warning(
                            f"[WARNING] Maximum re-tries reached: {self.re_tries}/{self.max_re_tries}, skipping step"
                        )
                        raise ValueError(
                            f"[ERROR] Maximum re-tries reached: {self.re_tries}/{self.max_re_tries}, stopping run."
                        )
                    # Restart the step. Should control re-try times.
                    self.sub_messages = deepcopy(self.base_dialog)
                    self.sub_messages.append(
                        {
                            "role": "user",
                            "content": self.l2mac_prompts.control_unit_execute_instruction.format(
                                step=step,
                                file_names=self.get_file_names(),
                                test_writing_advice=self.l2mac_prompts.test_writing_advice,
                                previous_step_output_summary=summary_step_message,
                                functions_provided=self.get_function_names_as_str(),
                            ),
                        }
                    )
                    response_message = self.get_llm_response(self.sub_messages)
                self.sub_messages.append(response_message)
                if response_message.get("tool_calls"):
                    function_return_messages, self.file_dict = process_function_call_and_return_message(
                        response_message["tool_calls"],
                        self.file_dict,
                        tools=self.functions,
                        enable_tests=self.run_tests,
                    )
                    for function_return_message in function_return_messages:
                        self.sub_messages.append(function_return_message)
                        if (
                            "status" in json.loads(function_return_message["content"])
                            and json.loads(function_return_message["content"])["status"] == "TASK_STEP_COMPLETE"
                        ):
                            task_step_complete = True
                            self.sub_messages.append(
                                {
                                    "role": "user",
                                    "content": self.l2mac_prompts.control_unit_instruction_complete_summarize_output,
                                }
                            )
                        elif (
                            "name" in function_return_message
                            and function_return_message["name"] == "sub_task_step_complete"
                            and json.loads(function_return_message["content"])["status"] == "error"
                        ):
                            self.sub_messages.append(
                                {
                                    "role": "user",
                                    "content": self.l2mac_prompts.control_unit_instruction_erroring_fix_the_code.format(
                                        error_message=json.loads(function_return_message["content"])["message"],
                                        file_names=self.get_file_names(),
                                        test_writing_advice=self.l2mac_prompts.test_writing_advice,
                                        functions_provided=self.get_function_names_as_str(),
                                    ),
                                }
                            )
                        else:
                            self.sub_messages.append(
                                {
                                    "role": "user",
                                    "content": self.l2mac_prompts.control_unit_cycle_message_to_check_if_instruction_complete.format(
                                        step=step,
                                        file_names=self.get_file_names(),
                                        functions_provided=self.get_function_names_as_str(),
                                    ),
                                }
                            )
                else:
                    self.sub_messages.append(
                        {
                            "role": "user",
                            "content": self.l2mac_prompts.control_unit_cycle_message_to_check_if_instruction_complete.format(
                                step=step,
                                file_names=self.get_file_names(),
                                functions_provided=self.get_function_names_as_str(),
                            ),
                        }
                    )
                write_files_from_dict(self.file_dict, base_dir=f"{self.folder_path}")
            self.logger.info("[STEP COMPLETE] sub step completed")
        self.logger.info("[TASK COMPLETE SUCCESSFULLY] All steps of prompt program complete")
        self.logger.info(f"You can run your new code at: {self.folder_path}")
        write_files_from_dict(self.file_dict, base_dir=f"{self.folder_path}")
        self.save_agent_state(self.sub_messages)
        return self.file_dict
