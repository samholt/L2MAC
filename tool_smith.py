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
from executor import pytest_code_base, python_run_code_base
from utils.checkpoint_utils import dump_locals_to_json
from llm_utils import num_tokens_from_functions
from openai.error import InvalidRequestError
from summarizer_and_modifier import fix_line_spacings, fix_indentation
from utils.indenter_utils import reindent_lines


class TestWritingTool(unittest.TestCase):


    def get_llm_response(self, messages, functions):
        # num_tokens = num_tokens_consumed_by_chat_request(messages=messages)
        logger = None
        name = "TestWritingTool"
        llm_config = get_llm_config(self.config, logger, name, self.rate_limiter)
        llm_config['messages'] = messages
        llm_config['temperature'] = 0.1
        llm_config['top_p'] = 1.0
        llm_config['functions'] = functions
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
        self.system_message = {"role": "system", "content": f'''
You are an expert code writing autonomous machine.

You must act autonomously and you will receive no human input at any stage. You can only use the defined functions to modify code to complete the task.

Use the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.
'''}

    def test_fix_this_file(self):
        messages = [self.system_message, {"role": "user", "content": """
Change the specified file.py from the existing file to the desired new file contents.

Existing file file.py```
1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot
2: from vehicle import Vehicle, VehicleSize
3: 
4: class Level:
5:     def __init__(self, spots):
6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
8: 
9:     def park_vehicle(self, vehicle):
10:         if isinstance(vehicle, Motorcycle):
11:             if self.available_spots[MotorcycleSpot] > 0:
12:                 self.available_spots[MotorcycleSpot] -= 1
13:                 return True
14:         elif isinstance(vehicle, Car):
15:             if self.available_spots[CompactSpot] > 0:
16:                 self.available_spots[CompactSpot] -= 1
17:                 return True
18:         elif isinstance(vehicle, Bus):
19:             if self.available_spots[LargeSpot] >= 5:
20:                 self.available_spots[LargeSpot] -= 5
21:                 return True
22:         return False
23: 
24:     def remove_vehicle(self, vehicle):
25:         if isinstance(vehicle, Motorcycle):
26:             self.available_spots[MotorcycleSpot] += 1
27:             return True
28:         elif isinstance(vehicle, Car):
29:             self.available_spots[CompactSpot] += 1
30:             return True
31:         elif isinstance(vehicle, Bus):
32:             self.available_spots[LargeSpot] += 5
33:             return True
34:         return False
```
                                          
Desired new file file.py```
+ 1: from vehicle import Motorcycle, Car, Bus
+ 2: 
+ 3: class Level:
+ 4:     def __init__(self, spots):
+ 5:         self.spots = spots
+ 6:         self.available_spots = {k: v for k, v in spots.items()}
+ 7: 
+ 8:     def park_vehicle(self, vehicle):
+ 9:         if isinstance(vehicle, Motorcycle):
+ 10:             if self.available_spots['MotorcycleSpot'] > 0:
+ 11:                 self.available_spots['MotorcycleSpot'] -= 1
+ 12:                 return True
+ 13:             elif self.available_spots['CompactSpot'] > 0:
+ 14:                 self.available_spots['CompactSpot'] -= 1
+ 15:                 return True
+ 16:             elif self.available_spots['LargeSpot'] > 0:
+ 17:                 self.available_spots['LargeSpot'] -= 1
+ 18:                 return True
+ 19:         elif isinstance(vehicle, Car):
+ 20:             if self.available_spots['CompactSpot'] > 0:
+ 21:                 self.available_spots['CompactSpot'] -= 1
+ 22:                 return True
+ 23:             elif self.available_spots['LargeSpot'] > 0:
+ 24:                 self.available_spots['LargeSpot'] -= 1
+ 25:                 return True
+ 26:         elif isinstance(vehicle, Bus):
+ 27:             if self.available_spots['LargeSpot'] >= 5:
+ 28:                 self.available_spots['LargeSpot'] -= 5
+ 29:                 return True
+ 30:         return False
+ 31: 
+ 32:     def remove_vehicle(self, vehicle):
+ 33:         if isinstance(vehicle, Motorcycle):
+ 34:             if self.spots['MotorcycleSpot'] > self.available_spots['MotorcycleSpot']:
+ 35:                 self.available_spots['MotorcycleSpot'] += 1
+ 36:                 return True
+ 37:             elif self.spots['CompactSpot'] > self.available_spots['CompactSpot']:
+ 38:                 self.available_spots['CompactSpot'] += 1
+ 39:                 return True
+ 40:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:
+ 41:                 self.available_spots['LargeSpot'] += 1
+ 42:                 return True
+ 43:         elif isinstance(vehicle, Car):
+ 44:             if self.spots['CompactSpot'] > self.available_spots['CompactSpot']:
+ 45:                 self.available_spots['CompactSpot'] += 1
+ 46:                 return True
+ 47:             elif self.spots['LargeSpot'] > self.available_spots['LargeSpot']:
+ 48:                 self.available_spots['LargeSpot'] += 1
+ 49:                 return True
+ 50:         elif isinstance(vehicle, Bus):
+ 51:             if self.spots['LargeSpot'] - 5 >= self.available_spots['LargeSpot']:
+ 52:                 self.available_spots['LargeSpot'] += 5
+ 53:                 return True
+ 54:         return False
```
""", 'function_call': {"name": 'write_files'}}]
        functions = [{
            "name": "write_files",
            "description": "Write out multiple files. Use the diff format using line numbers, and it will be combined into the existing code base.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_and_contents": {
                        "type": "array",
                        "description": 'list of files and their contents in diff format using line numbers, each as a dictionary to write. When writing any code you will always give it in diff format, with line numbers. For example. Adding (appending) two new lines to a new file is """+ 1: import time\n+ : import os""". Replacing a line is """r 8: import sys""". Deleting multiple lines from line 5 to 10 is """- 5-10""".',
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
        response_message = self.get_llm_response(messages, functions)
        print(response_message)
        print('')

    def test_fix_this_file_minor_change(self):
        messages = [self.system_message, {"role": "user", "content": """
Change the specified file.py from the existing file to the desired new file contents respond only with the function call.

Existing file file.py```
1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot
2: from vehicle import Vehicle, VehicleSize
3: 
4: class Level:
5:     def __init__(self, spots):
6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
8: 
9:     def park_vehicle(self, vehicle):
10:         if isinstance(vehicle, Motorcycle):
11:             if self.available_spots[MotorcycleSpot] > 0:
12:                 self.available_spots[MotorcycleSpot] -= 1
13:                 return True
14:         elif isinstance(vehicle, Car):
15:             if self.available_spots[CompactSpot] > 0:
16:                 self.available_spots[CompactSpot] -= 1
17:                 return True
18:         elif isinstance(vehicle, Bus):
19:             if self.available_spots[LargeSpot] >= 5:
20:                 self.available_spots[LargeSpot] -= 5
21:                 return True
22:         return False
23: 
24:     def remove_vehicle(self, vehicle):
25:         if isinstance(vehicle, Motorcycle):
26:             self.available_spots[MotorcycleSpot] += 1
27:             return True
28:         elif isinstance(vehicle, Car):
29:             self.available_spots[CompactSpot] += 1
30:             return True
31:         elif isinstance(vehicle, Bus):
32:             self.available_spots[LargeSpot] += 5
33:             return True
34:         return False
```
                                          
Desired new file file.py```
1: from parking_spot import MotorcycleSpot, CompactSpot, LargeSpot
2: from vehicle import Vehicle, VehicleSize
3: 
4: class Level:
5:     def __init__(self, spots):
6:         self.spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
7:         self.available_spots = {MotorcycleSpot: spots['MotorcycleSpot'], CompactSpot: spots['CompactSpot'], LargeSpot: spots['LargeSpot']}
8: 
9:     def park_vehicles(self, vehicle):
10:         if isinstance(vehicle, Motorcycle):
11:             if self.available_spots[MotorcycleSpot] > 0:
12:                 self.available_spots[MotorcycleSpot] -= 1
13:                 return True
14:         elif isinstance(vehicle, Car):
15:             if self.available_spots[CompactSpot] > 0:
16:                 self.available_spots[CompactSpot] -= 1
17:                 return True
18:         elif isinstance(vehicle, Bus):
19:             if self.available_spots[LargeSpot] >= 5:
20:                 self.available_spots[LargeSpot] -= 5
21:                 return True
22:         return False
23: 
24:     def remove_vehicle_all_the_way(self, vehicle):
25:         if isinstance(vehicle, Motorcycle):
26:             self.available_spots[MotorcycleSpot] += 1
27:             return True
28:         elif isinstance(vehicle, Car):
29:             self.available_spots[CompactSpot] += 1
30:             return False
31:         elif isinstance(vehicle, Bus):
32:             self.available_spots[LargeSpot] += 5
33:             return True
34:         return False
```
""", 'function_call': {"name": 'write_files'}}]
        functions = [{
            "name": "write_files",
            "description": "Write out multiple files. Use the diff format using line numbers, and it will be combined into the existing code base.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_and_contents": {
                        "type": "array",
                        "description": 'list of files and their contents in diff format using line numbers, each as a dictionary to write. When writing any code you will always give it in diff format, with line numbers. For example. Adding (appending) two new lines to a new file is """+ 1: import time\n+ : import os""". Replacing a line is """r 8: def fruit(name):""". Deleting multiple lines from line 5 to 10 is """- 5-10""".',
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
        response_message = self.get_llm_response(messages, functions)
        print(response_message)
        print('')
    
    def fix_corner_case_of_not_deleting_before_writing(self):
        messages = [{'role': 'system', 'content': '\nObjective: Write code for a large system design task.\n\nYou must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task, and correctly incorporate it into the existing code base.\n         \nWhen writing any code you will always give it in diff format, with line numbers. For example. Replacing a line is """r 8: def fruit(name):""". Deleting multiple lines from line 5 to 10 is """- 5-10""". Appending two new lines to a file is """+ 5: import time\n+ 6: import os""". If you wish to overwrite the existing file (delete it completely and then add the new lines), please specify overwrite_file to True.\n                          \nWhen modifying code and including new code, you must use the diff format using the line numbers.\nPlease always view the files before writing to them, to make sure you are writing to the correct files.\nIf you are unsure, you can list all available files to view with the `list_files` function.\n\nProvide the minimal code necessary to achieve the task conditioned on the existing generated code---including changing the existing generated code.\n\nYou cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.\n\nYou can write to local files, however you cannot use any databases, as none are setup in the local environment.\n                          \nUse the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.\n'}, {'role': 'user', 'content': '\nYou will get instructions for code to write.\nYou will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.\n\nThink step by step and reason yourself to the right decisions to make sure we get it right.\nFirst lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.\n\nDo not comment on what every file does. Please note that the code should be fully functional. No placeholders.\n\nYou will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.\nPlease note that the code should be fully functional. No placeholders.\n\nFollow a language and framework appropriate best practice file naming convention.\nMake sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.\nWhen writing code if you are unsure, write a plausible implementation.\nInclude module dependency or package manager dependency definition file.\n\nUseful to know:\n                        \nAlways use the programming language the user asks for.\nFor Python, you always create an appropriate requirements.txt file.\nFor NodeJS, you always create an appropriate package.json file.\nAlways add a comment briefly describing the purpose of the function definition.\nAdd comments explaining very complex bits of logic.\nAlways follow the best practices for the requested languages for folder/file structure and how to package the project.\n\n\nPython toolbelt preferences:\n- pytest\n- dataclasses\n\nObjective:```\nWrite complete MVC code for the following system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)\nFeatures to implement: \n1. One-on-one text messaging between users.\n2. Support group chats.\n3. Delivered and read status\n4. Support sending .jpg images between users.\n5. End-to-end message encryption.\n```\n                        \nUnderstand the problem, by creating a detailed step-by-step plan. Try to solve the problem in the minimal steps necessary, in no more than 10 steps. Create additional tests, and run the tests at each step when applicable. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once. The last step should be running any tests if they exist. Only create a detailed plan to begin with, which includes designing and running tests to check that they all pass.                              \n'}, {'role': 'assistant', 'function_call': {'name': 'provide_detailed_sub_task_steps_for_sub_agents', 'arguments': '\n{\n  "steps": [\n    "Step 1: Create the core classes and their methods for the chat service. This includes User, Message, Chat, GroupChat, and ImageMessage classes. Also, create a Controller class to handle the logic of the application.",\n    "Step 2: Implement the User class with attributes such as id, name, and a list of chats. Include methods to send a message, read a message, and get the status of a message.",\n    "Step 3: Implement the Message class with attributes such as id, sender, receiver, content, timestamp, delivered status, and read status. Include methods to mark the message as delivered and read.",\n    "Step 4: Implement the Chat class with attributes such as id, participants, and a list of messages. Include methods to add a message, get a message, and get all messages.",\n    "Step 5: Implement the GroupChat class that inherits from the Chat class. Modify the participants attribute to hold multiple users and adjust the methods accordingly.",\n    "Step 6: Implement the ImageMessage class that inherits from the Message class. Add an attribute for the image file and adjust the methods accordingly.",\n    "Step 7: Implement the Controller class with methods to create a user, create a chat, send a message, read a message, get the status of a message, and send an image message.",\n    "Step 8: Implement end-to-end encryption for the messages. This can be done by adding encryption and decryption methods in the Message class and calling them when sending and reading a message respectively.",\n    "Step 9: Write tests for all the classes and methods. Use pytest for this.",\n    "Step 10: Run the tests to ensure that all the features are working as expected."\n  ]\n}'}, 'content': None}, {'role': 'user', 'content': "\nExecute step: Step 8: Implement end-to-end encryption for the messages. This can be done by adding encryption and decryption methods in the Message class and calling them when sending and reading a message respectively. \n\n Condition it on existing code files: ['user.py', 'message.py', 'chat.py', 'group_chat.py', 'image_message.py', 'controller.py']\nPlease now select which files you want to view, and view them.\n"}, {'role': 'assistant', 'function_call': {'name': 'view_files', 'arguments': '\n{\n  "files": ["user.py", "message.py", "chat.py", "group_chat.py", "image_message.py", "controller.py"]\n}'}, 'content': None}, {'role': 'function', 'name': 'view_files', 'content': '{"files": "user.py\\n```python\\n1: class User:\\n2:     def __init__(self, id, name):\\n3:         self.id = id\\n4:         self.name = name\\n5:         self.chats = []\\n6: \\n7:     def send_message(self, chat_id, content):\\n8:         for chat in self.chats:\\n9:             if chat.id == chat_id:\\n10:                 chat.add_message(self.id, content)\\n11:                 break\\n12: \\n13:     def read_message(self, chat_id, message_id):\\n14:         for chat in self.chats:\\n15:             if chat.id == chat_id:\\n16:                 message = chat.get_message(message_id)\\n17:                 if message:\\n18:                     message.mark_as_read()\\n19:                 break\\n20: \\n21:     def get_status(self, chat_id, message_id):\\n22:         for chat in self.chats:\\n23:             if chat.id == chat_id:\\n24:                 message = chat.get_message(message_id)\\n25:                 if message:\\n26:                     return message.delivered, message.read\\n27:                 break\\n28:         return None, None\\n```\\n\\nmessage.py\\n```python\\n1: import datetime\\n2: \\n3: class Message:\\n4:     def __init__(self, id, sender, receiver, content):\\n5:         self.id = id\\n6:         self.sender = sender\\n7:         self.receiver = receiver\\n8:         self.content = content\\n9:         self.timestamp = datetime.datetime.now()\\n10:         self.delivered = False\\n11:         self.read = False\\n12: \\n13:     def mark_as_delivered(self):\\n14:         self.delivered = True\\n15: \\n16:     def mark_as_read(self):\\n17:         self.read = True\\n```\\n\\nchat.py\\n```python\\n1: class Chat:\\n2:     def __init__(self, id, participants):\\n3:         self.id = id\\n4:         self.participants = participants\\n5:         self.messages = []\\n6: \\n7:     def add_message(self, message):\\n8:         pass\\n9: \\n10:     def get_message(self, message_id):\\n11:         pass\\n12: \\n13:     def get_all_messages(self):\\n14:         pass\\n```\\n\\ngroup_chat.py\\n```python\\n1: from chat import Chat\\n2: \\n3: class GroupChat(Chat):\\n4:     def __init__(self, id, participants):\\n5:         super().__init__(id, participants)\\n6:         super().__init__(id, participants)\\n7:         self.participants = list(participants)\\n\\n8:     def add_message(self, sender_id, content):\\n9:         message = Message(len(self.messages), sender_id, self.id, content)\\n10:         self.messages.append(message)\\n11:         for participant in self.participants:\\n12:             if participant.id != sender_id:\\n13:                 participant.receive_message(self.id, message)\\n\\n14:     def get_message(self, message_id):\\n15:         for message in self.messages:\\n16:             if message.id == message_id:\\n17:                 return message\\n18:         return None\\n\\n19:     def get_all_messages(self):\\n20:         return self.messages\\n```\\n\\nimage_message.py\\n```python\\n1: from message import Message\\n2: \\n3: class ImageMessage(Message):\\n4:     def __init__(self, id, sender, receiver, content, image_file):\\n5:         super().__init__(id, sender, receiver, content)\\n6:         self.image_file = image_file\\n```\\n\\ncontroller.py\\n```python\\n1: class Controller:\\n2:     def __init__(self):\\n3:         self.users = []\\n4:         self.chats = []\\n5: \\n6:     def create_user(self):\\n7:         pass\\n8: \\n9:     def create_chat(self):\\n10:         pass\\n11: \\n12:     def send_message(self):\\n13:         pass\\n14: \\n15:     def read_message(self):\\n16:         pass\\n17: \\n18:     def get_status(self):\\n19:         pass\\n20: \\n21:     def send_image_message(self):\\n22:         pass\\n```\\n\\n"}'}, {'role': 'user', 'content': "\nHas the task been completed of: ```\nStep 8: Implement end-to-end encryption for the messages. This can be done by adding encryption and decryption methods in the Message class and calling them when sending and reading a message respectively.\n``` \n\n If yes, return ACCEPT, otherwise reflect and return the full complete corrected code to complete the task, use the defined functions to write the code. Condition it on existing code: ['user.py', 'message.py', 'chat.py', 'group_chat.py', 'image_message.py', 'controller.py']. If you have not viewed the files before writing to them, please view them, to make sure you are writing to the correct files.\n"}]
        file_dict = {'user.py': ['1: class User:', '2:     def __init__(self, id, name):', '3:         self.id = id', '4:         self.name = name', '5:         self.chats = []', '6: ', '7:     def send_message(self, chat_id, content):', '8:         for chat in self.chats:', '9:             if chat.id == chat_id:', '10:                 chat.add_message(self.id, content)', '11:                 break', '12: ', '13:     def read_message(self, chat_id, message_id):', '14:         for chat in self.chats:', '15:             if chat.id == chat_id:', '16:                 message = chat.get_message(message_id)', '17:                 if message:', '18:                     message.mark_as_read()', '19:                 break', '20: ', '21:     def get_status(self, chat_id, message_id):', '22:         for chat in self.chats:', '23:             if chat.id == chat_id:', '24:                 message = chat.get_message(message_id)', '25:                 if message:', '26:                     return message.delivered, message.read', '27:                 break', '28:         return None, None'], 'message.py': ['1: import datetime', '2: ', '3: class Message:', '4:     def __init__(self, id, sender, receiver, content):', '5:         self.id = id', '6:         self.sender = sender', '7:         self.receiver = receiver', '8:         self.content = content', '9:         self.timestamp = datetime.datetime.now()', '10:         self.delivered = False', '11:         self.read = False', '12: ', '13:     def mark_as_delivered(self):', '14:         self.delivered = True', '15: ', '16:     def mark_as_read(self):', '17:         self.read = True'], 'chat.py': ['1: class Chat:', '2:     def __init__(self, id, participants):', '3:         self.id = id', '4:         self.participants = participants', '5:         self.messages = []', '6: ', '7:     def add_message(self, message):', '8:         pass', '9: ', '10:     def get_message(self, message_id):', '11:         pass', '12: ', '13:     def get_all_messages(self):', '14:         pass'], 'group_chat.py': ['1: from chat import Chat', '2: ', '3: class GroupChat(Chat):', '4:     def __init__(self, id, participants):', '5:         super().__init__(id, participants)', '6:         super().__init__(id, participants)', '7:         self.participants = list(participants)\n', '8:     def add_message(self, sender_id, content):', '9:         message = Message(len(self.messages), sender_id, self.id, content)', '10:         self.messages.append(message)', '11:         for participant in self.participants:', '12:             if participant.id != sender_id:', '13:                 participant.receive_message(self.id, message)\n', '14:     def get_message(self, message_id):', '15:         for message in self.messages:', '16:             if message.id == message_id:', '17:                 return message', '18:         return None\n', '19:     def get_all_messages(self):', '20:         return self.messages'], 'image_message.py': ['1: from message import Message', '2: ', '3: class ImageMessage(Message):', '4:     def __init__(self, id, sender, receiver, content, image_file):', '5:         super().__init__(id, sender, receiver, content)', '6:         self.image_file = image_file'], 'controller.py': ['1: class Controller:', '2:     def __init__(self):', '3:         self.users = []', '4:         self.chats = []', '5: ', '6:     def create_user(self):', '7:         pass', '8: ', '9:     def create_chat(self):', '10:         pass', '11: ', '12:     def send_message(self):', '13:         pass', '14: ', '15:     def read_message(self):', '16:         pass', '17: ', '18:     def get_status(self):', '19:         pass', '20: ', '21:     def send_image_message(self):', '22:         pass']}
        functions = [{
            "name": "write_files",
            "description": "Write out multiple files. Use the diff format using line numbers, and it will be combined into the existing code base. You always indent code with tabs, using the `\t` character.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_and_contents": {
                        "type": "array",
                        "description": 'list of files and their contents in diff format using line numbers, each as a dictionary to write. When writing any code you will always give it in diff format, with line numbers. For example. Replacing a line is """r 8: def fruit(name):""". Deleting multiple lines from line 5 to 10 is """- 5-10""". Appending two new lines to a file is """+ 5: import time\n+ 6: import os""". If you wish to overwrite the existing file (delete it completely and then add the new lines), please specify overwrite_file to True.',
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
        },]
        response_message = self.get_llm_response(messages, functions)
        print(response_message)
        function_args = json.loads(response_message["function_call"]["arguments"])
        from utils.llm_tools import write_files
        output, new_file_dict = write_files(function_args["files_and_contents"], file_dict)

    def fix_failing_to_overwrite_file(self):
        messages = [{'role': 'system', 'content': '\nObjective: Write code for a large system design task.\n\nYou must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task, and correctly incorporate it into the existing code base.\n\nYou always write out the whole file contents. You always indent code with tabs.\n\nPlease always view the files before writing to them, to make sure you are writing to the correct files.\nIf you are unsure, you can list all available files to view with the `list_files` function.\n\nProvide the minimal code necessary to achieve the task conditioned on the existing generated code---including changing the existing generated code.\n\nYou cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.\n\nYou can write to local files, however you cannot use any databases, as none are setup in the local environment.\n\nUse the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.\n'}, {'role': 'user', 'content': '\nYou will get instructions for code to write.\nYou will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.\n\nThink step by step and reason yourself to the right decisions to make sure we get it right.\nFirst lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.\n\nDo not comment on what every file does. Please note that the code should be fully functional. No placeholders.\n\nYou will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.\nPlease note that the code should be fully functional. No placeholders.\n\nFollow a language and framework appropriate best practice file naming convention.\nMake sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.\nWhen writing code if you are unsure, write a plausible implementation.\nInclude module dependency or package manager dependency definition file.\n\nUseful to know:\n\nAlways use the programming language the user asks for.\nFor Python, you always create an appropriate requirements.txt file.\nFor NodeJS, you always create an appropriate package.json file.\nAlways add a comment briefly describing the purpose of the function definition.\nAdd comments explaining very complex bits of logic.\nAlways follow the best practices for the requested languages for folder/file structure and how to package the project.\nYou can use any package and any other packages you wish to install.\n\nPython toolbelt preferences:\n- pytest\n- dataclasses\n\nObjective:```\nWrite complete MVC code for the following system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)\nFeatures to implement: \n1. One-on-one text messaging between users.\n2. Support group chats.\n3. Delivered and read status\n4. Support sending .jpg images between users.\n5. End-to-end message encryption.\n```\n\nUnderstand the problem, by creating a detailed step-by-step plan. Try to solve the problem in the minimal steps necessary, in no more than 10 steps. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation, where all the code is fully functional. Use best software design practices, and you can output large amounts of code at once. The last step should be running any tests automatically if they exist, and the penultimate step writing these tests. You will receive no human input at any stage, so you cannot use a human to test. Only create a detailed plan to begin with, which includes designing and running tests to check that they all pass.\n'}, {
  "role": "assistant",
  "function_call": {
    "name": "provide_detailed_sub_task_steps_for_sub_agents",
    "arguments": "{\n  \"steps\": [\n    \"1. Define the core classes and their methods for the chat service. This includes User, Message, Chat, GroupChat, and Image classes. Also, define the encryption and decryption methods for end-to-end encryption.\",\n    \"2. Implement the User class with attributes such as user_id, name, and a list of chats. The User class should have methods to send a message, read a message, and create a group chat.\",\n    \"3. Implement the Message class with attributes such as message_id, sender, recipient, content, timestamp, delivered status, and read status. The Message class should have methods to mark as delivered, mark as read, and encrypt the message content.\",\n    \"4. Implement the Chat class with attributes such as chat_id, participants, and a list of messages. The Chat class should have methods to add a message, get a message, and get all messages.\",\n    \"5. Implement the GroupChat class which inherits from the Chat class. The GroupChat class should have additional methods to add a participant and remove a participant.\",\n    \"6. Implement the Image class with attributes such as image_id, sender, recipient, image_path, timestamp, delivered status, and read status. The Image class should inherit from the Message class and override the encryption method to handle image encryption.\",\n    \"7. Implement the encryption and decryption methods. Use a symmetric encryption algorithm such as AES for simplicity. The encryption key can be a shared secret between the sender and the recipient.\",\n    \"8. Write unit tests for each class and method. Use pytest for writing the tests. The tests should cover all the features of the chat service.\",\n    \"9. Run the unit tests using pytest. Ensure that all the tests pass.\",\n    \"10. Package the project and generate a requirements.txt file. The requirements.txt file should list all the dependencies of the project.\"\n  ]\n}"
  },
  "content": None
}, {'role': 'user', 'content': "\nObjective: Execute task step: 2. Implement the User class with attributes such as user_id, name, and a list of chats. The User class should have methods to send a message, read a message, and create a group chat. \n\n Note: Condition any new code files on the existing code files: ['user.py', 'message.py', 'chat.py', 'group_chat.py', 'image.py', 'encryption.py']. You can now optionally view the existing files if you need to view them to complete the current task step. You have a limited context window so be selective about which files you view, only view the files you think you might need to view.\n"}, {
  "role": "assistant",
  "function_call": {
    "name": "view_files",
    "arguments": "{\n  \"files\": [\"user.py\"]\n}"
  },
  "content": None
}, {'role': 'function', 'name': 'view_files', 'content': '{"files": "user.py\\n```python\\n1: from typing import List\\n\\n2: \\n3: class User:\\n4: \\tdef __init__(self, user_id: str, name: str):\\n5: \\t\\tself.user_id = user_id\\n6: \\t\\tself.name = name\\n7: \\t\\tself.chats = []\\n\\n8: \\tdef send_message(self, recipient, content):\\n9: \\t\\tpass\\n\\n10: \\tdef read_message(self, message):\\n11: \\t\\tpass\\n\\n12: \\tdef create_group_chat(self, participants: List[str]):\\n13: \\t\\tpass\\n```\\n\\n"}'}, {'role': 'user', 'content': "\nHas the task been completed of: ```\n2. Implement the User class with attributes such as user_id, name, and a list of chats. The User class should have methods to send a message, read a message, and create a group chat.\n``` \n\n If yes, return ACCEPT, otherwise reflect and return the full complete corrected code to complete the task, use the defined functions to write the code. Condition it on existing code: ['user.py', 'message.py', 'chat.py', 'group_chat.py', 'image.py', 'encryption.py']. If you have not viewed the files before writing to them, please view them, to make sure you are writing to the correct files.\n", 'function_call': {"name": 'write_files'}}]
        functions = [{
            "name": "write_files",
            "description": "Write out multiple files and it will be combined into the existing code base. Always output the whole file. You always indent code with tabs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "files_and_contents": {
                        "type": "array",
                        "description": 'list of files and their contents.',
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
        response_message = self.get_llm_response(messages, functions)
        # print(response_message)
        function_args = json.loads(response_message["function_call"]["arguments"])
        print(json.loads(messages[-2]['content'])['files'])
        print('=========\n')
        print(function_args["files_and_contents"][0]['file_contents'])
        from utils.llm_tools import write_files
        output, new_file_dict = write_files(function_args["files_and_contents"], file_dict)
        print('')
        
    def tune_deleting_files(self):
        messages = [{'role': 'system', 'content': '\nObjective: Write code for a large system design task.\n\nYou must act autonomously and you will receive no human input at any stage. You have to return as output the complete code for completing this task, and correctly incorporate it into the existing code base.\n\nYou always write out the whole file contents. You always indent code with tabs.\n\nPlease always view the files before writing to them, to make sure you are writing to the correct files.\nIf you are unsure, you can list all available files to view with the `list_files` function.\n\nProvide the minimal code necessary to achieve the task conditioned on the existing generated code---including changing the existing generated code.\n\nYou cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.\n\nYou can write to local files, however you cannot use any databases, as none are setup in the local environment.\n\nUse the functions provided. When calling functions only provide a RFC8259 compliant JSON request following this format without deviation.\n'}, {'role': 'user', 'content': '\nYou will get instructions for code to write.\nYou will write a very long answer. Make sure that every detail of the architecture is, in the end, implemented as code.\n\nThink step by step and reason yourself to the right decisions to make sure we get it right.\nFirst lay out the names of the core classes, functions, methods that will be necessary, As well as a quick comment on their purpose.\n\nDo not comment on what every file does. Please note that the code should be fully functional. No placeholders.\n\nYou will start with the "entrypoint" file, then go to the ones that are imported by that file, and so on.\nPlease note that the code should be fully functional. No placeholders.\n\nFollow a language and framework appropriate best practice file naming convention.\nMake sure that files contain all imports, types etc.  The code should be fully functional. Make sure that code in different files are compatible with each other.\nWhen writing code if you are unsure, write a plausible implementation.\nInclude module dependency or package manager dependency definition file.\n\nUseful to know:\n\nAlways use the programming language the user asks for.\nFor Python, you always create an appropriate requirements.txt file.\nFor NodeJS, you always create an appropriate package.json file.\nAlways add a comment briefly describing the purpose of the function definition.\nAdd comments explaining very complex bits of logic.\nAlways follow the best practices for the requested languages for folder/file structure and how to package the project.\nYou can use any package and any other packages you wish to install.\n\nPython toolbelt preferences:\n- pytest\n- dataclasses\n\nObjective:```\nWrite complete MVC code for the following system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)\nFeatures to implement: \n1. One-on-one text messaging between users.\n2. Support group chats.\n3. Delivered and read status\n4. Support sending .jpg images between users.\n5. End-to-end message encryption.\n```\n\nUnderstand the problem, by creating a detailed step-by-step plan. Try to solve the problem in the minimal steps necessary, in no more than 10 steps. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation, where all the code is fully functional. Use best software design practices, and you can output large amounts of code at once. The last step should be running any tests automatically if they exist, and the penultimate step writing these tests. You will receive no human input at any stage, so you cannot use a human to test. Only create a detailed plan to begin with, which includes designing and running tests to check that they all pass.\n'}, {'role': 'user', 'content': "\nObjective: Execute task step: 2. Delete all files, by using the `-1` command. \n\n Note: Condition any new code files on the existing code files: ['user.py', 'message.py', 'chat.py', 'group_chat.py', 'image.py', 'encryption.py']. You can now optionally view the existing files if you need to view them to complete the current task step. You have a limited context window so be selective about which files you view, only view the files you think you might need to view.\n", 'function_call': {"name": 'delete_files'}},]
        functions = [{
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
        response_message = self.get_llm_response(messages, functions)
        # print(response_message)
        function_args = json.loads(response_message["function_call"]["arguments"])
        print(json.loads(messages[-2]['content'])['files'])
        print('=========\n')
        print(function_args["files_and_contents"][0]['file_contents'])
        print('')

# Run the tests
if __name__ == '__main__':
    # unittest.main()

    cls = TestWritingTool()
    cls.setUp()
    cls.tune_deleting_files()


            