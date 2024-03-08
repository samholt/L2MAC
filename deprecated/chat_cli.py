#!/bin/env python

import hydra
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

from pathlib import Path
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.history import FileHistory
from rich.console import Console
from rich.markdown import Markdown

from llm_utils import setup_chat_rate_limiter, chat_completion_rl, get_llm_config, num_tokens_consumed_by_chat_request, get_model_max_tokens







@hydra.main(version_base=None, config_path="config", config_name="config.yaml")
def run(config: DictConfig) -> None:
    log_path = generate_log_file_path(__file__, log_folder=config.setup.log_dir, config=config)
    logger = create_logger_in_process(log_path)
    request_limit, token_limit = setup_chat_rate_limiter(config)
    max_tokens = get_model_max_tokens(config)
    rate_limiter = ChatRateLimiter(request_limit=request_limit, token_limit=token_limit)
    config.run.log_path = log_path
    seed_all(0)
    console = Console()
    console.print("ChatGPT CLI", style="bold")
    # HISTORY_FILE = "./history"
    # history = FileHistory(HISTORY_FILE)
    # session = PromptSession(history=history, multiline=True)
    session = PromptSession(multiline=True)

    console.rule()

    
    # messages = [
    #     {"role": "system", "content": "Always use code blocks with the appropriate language tags. If asked for a table always format it using Markdown syntax."},
    #     {"role": "user", "content": "Please give me multiple system design questions. Please provide high level descriptions of possible unit tests, and integration tests to verify the successful completion of each system design question."},
    #                     ]

    messages = [
        {"role": "system", "content": f"""
Objective: Write python code for a large system design task.

You must act autonomously and you will receive no human input at any stage. You have to return as output the complete python code for completing this task. 
         
When generating code, specify the git diff format, and it will be combined into the existing code base.

1. EXECUTE_LINES: Executes the given python code only and returns the std out to you. You can see variables by printing them.
2. EXECUTE_FULL_CODE: Executes the current python file `main.py` and returns all results back to you. This is useful if you have written unit tests and you want to run everything to see if all the tests pass.

To use a tool, give the command, followed by the code in backticks, and then stop token of ##. This will then be executed and the result given to you. Only print small outputs, as large outputs will be truncated. Provide the minimal code necessary to achieve the task. When executing code include all library imports and previous code you wish to use, as the code is executed in a new python process without history of the previous commands executed.

You cannot visualize any graphical output. You exist within a Actor Model machine, and when you list out steps, each step will be taken by a new separate sub-ChatGPT model. When you list out a sub-task steps, you can optionally specify the sub-task validation to check that it has been completed successfully.

You can write to local files, however you cannot use any databases, as none are setup in the local environment. 
"""},
    {"role": "user", "content": """
Objective: Write complete python code for the following backend system design task. Design Facebook Messenger or WhatsApp (A Global Chat Service)
Things to include: 
* Approach for one-on-one text messaging between users.
* Approach for extending the design to support group chats.
* Delivered and read status
* What action needs to be taken if the user is not connected to the internet?
* Push notifications
* Sending media like images or other documents
* Approach for providing end-to-end message encryption.

Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once."""},
{
  "role": "assistant",
  "content": "We need to break our chat service down into a basic requirement and then implement other features.\n\nHere's a simplified list of what we need to build:\n\n1. User management system: Ability for users to register, keep their profile, add friends etc.\n2. Text Messaging: One to one text messaging system\n3. Group messaging: A group chat system\n4. Message Status: Show message delivery and read status\n5. Offline Handling: Store undelivered messages and deliver when user is online\n6. Push Notifications: Notify users of new messages\n7. Media Messages: Support for sending images and documents\n8. End-to-End Encryption: Secure the chat messages\n\nThis system will need three databases:\n\n1. User Database: This will contain profiles of the users including their usernames, passwords, online status etc.\n2. Message Database: This will contain the messages. Each message will be associated with a sender and a receiver.\n3. Group Database: This will contain the group chats. Each group will have its group members.\n\nPython `socket` and `requests` libraries can be used to handle messaging, while `sqlite3` can be used as a lightweight database. `pycrypto` library can be used for implementing End-to-End Encryption.\n\nHere's a simplified plan to get started, it's quite high level and will need a lot of detail filled in:\n\n1. Create a User model for the user database.\n2. Write functionality to Authenticate and Register a user.\n3. Create a Message model for the message database.\n4. Write functionality for a user to send a message to another user.\n5. Write functionality to check for messages for a given user.\n6. Create a Group model for the groups.\n7. Write functionality for creating a group and adding/removing users.\n8. Write functionality to send a message to a group.\n9. Write functionality to check for group messages.\n10. Write functionality to check message delivery and read status.\n11. Write functionality to store undelivered messages and deliver when user is online.\n12. Write functionality to send push notifications when new message is received.\n13. Write functionality to send images and documents in the messages.\n14. Implement End-to-End Encryption for message transmission.\n\nFor managing real-time connections, we can use a popular web application framework such as Flask (for simplicity) along with SocketIO which is a library that enables real-time, bidirectional and event-based communication between the browser and the server.\n\n"
},
{'role': 'user', 'content': 'Execute step 2. \n\n Condition it on the following code files: \n\nFile: `user.py`\n```diff\n+1\timport sqlite3\n+2\tfrom sqlite3 import Error\n+3\t\n+4\tclass User:\n+5\t    """\n+6\t    A user is someone with an account\n+7\t    They will be able to have a friends list in the future\n+8\t    """\n+9\t    def __init__(self, username, password):\n+10\t        self.username = username\n+11\t        self.password = password # we would want to hash this in production\n+12\t\n+13\t    def save(self):\n+14\t        """\n+15\t        Save User instance to the database\n+16\t        """\n+17\t        conn = None\n+18\t        try:\n+19\t            conn = sqlite3.connect(\'chat.db\') # connect to the sqlite3 database\n+20\t            print(sqlite3.version)\n+21\t        except Error as e:\n+22\t            print(e)\n+23\t\n+24\t        if conn:\n+25\t            try:\n+26\t                # Create table if it doesn\'t exist\n+27\t                conn.execute(\'\'\'\n+28\t                    CREATE TABLE IF NOT EXISTS users (\n+29\t                        username TEXT PRIMARY KEY,\n+30\t                        password TEXT NOT NULL\n+31\t                    )\n+32\t                \'\'\')\n+33\t                conn.commit()\n+34\t\n+35\t                # Save user to the database\n+36\t                conn.execute(f\'\'\'\n+37\t                    INSERT INTO users(username, password)\n+38\t                    VALUES(?, ?)\n+39\t                \'\'\', (self.username, self.password))\n+40\t                conn.commit()\n+41\t            except Error as e:\n+42\t                print(e)\n```\n\nFile: `main.py`\n```diff\n+1\tfrom user import User\n+2\t\n+3\t# Let\'s create a user\n+4\tuser = User(\'test\', \'password\')\n+5\tuser.save()\n```\n\nFile: `test_user.py`\n```diff\n+1\timport unittest\n+2\timport sqlite3\n+3\tfrom user import User\n+4\t\n+5\tclass TestUserMethods(unittest.TestCase):\n+6\t    \n+7\t    def test_save(self):\n+8\t        # create a test user\n+9\t        user = User(\'test\', \'password\')\n+10\t        user.save()\n+11\t\n+12\t        conn = sqlite3.connect(\'chat.db\') # connect to the sqlite3 database\n+13\t        cur = conn.cursor()\n+14\t        \n+15\t        # query for the test user\n+16\t        cur.execute("SELECT * FROM users WHERE username=?", (\'test\',))\n+17\t        row = cur.fetchone()\n+18\t        \n+19\t        self.assertIsNotNone(row) # assert not none\n+20\t        self.assertEqual(row[0], \'test\') # check username\n+21\t        self.assertEqual(row[1], \'password\') # check password\n+22\t\n+23\tif __name__ == \'__main__\':\n+24\t    unittest.main()\n```'},
# {'role': 'user', 'content': 'Execute step 2. \n\n Condition it on the following code files: \n\nFile: `user.py`\n```python\nimport sqlite3\nfrom sqlite3 import Error\n\nclass User:\n    """\n    A user is someone with an account\n    They will be able to have a friends list in the future\n    """\n    def __init__(self, username, password):\n        self.username = username\n        self.password = password # we would want to hash this in production\n\n    def save(self):\n        """\n        Save User instance to the database\n        """\n        conn = None\n        try:\n            conn = sqlite3.connect(\'chat.db\') # connect to the sqlite3 database\n            print(sqlite3.version)\n        except Error as e:\n            print(e)\n\n        if conn:\n            try:\n                # Create table if it doesn\'t exist\n                conn.execute(\'\'\'\n                    CREATE TABLE IF NOT EXISTS users (\n                        username TEXT PRIMARY KEY,\n                        password TEXT NOT NULL\n                    )\n                \'\'\')\n                conn.commit()\n\n                # Save user to the database\n                conn.execute(f\'\'\'\n                    INSERT INTO users(username, password)\n                    VALUES(?, ?)\n                \'\'\', (self.username, self.password))\n                conn.commit()\n            except Error as e:\n                print(e)\n```\n\nFile: `main.py`\n```python\nfrom user import User\n\n# Let\'s create a user\nuser = User(\'test\', \'password\')\nuser.save()\n```\n\nFile: `test_user.py`\n```python\nimport unittest\nimport sqlite3\nfrom user import User\n\nclass TestUserMethods(unittest.TestCase):\n    \n    def test_save(self):\n        # create a test user\n        user = User(\'test\', \'password\')\n        user.save()\n\n        conn = sqlite3.connect(\'chat.db\') # connect to the sqlite3 database\n        cur = conn.cursor()\n        \n        # query for the test user\n        cur.execute("SELECT * FROM users WHERE username=?", (\'test\',))\n        row = cur.fetchone()\n        \n        self.assertIsNotNone(row) # assert not none\n        self.assertEqual(row[0], \'test\') # check username\n        self.assertEqual(row[1], \'password\') # check password\n\nif __name__ == \'__main__\':\n    unittest.main()\n```'},
#     {"role": "user", "content": """
# Objective: Write complete python code for the following backend system design task. Design Pastebin.com.
# ### Use cases
# * **User** enters a block of text and gets a randomly generated link
#     * Expiration
#         * Default setting does not expire
#         * Can optionally set a timed expiration
# * **User** enters a paste's url and views the contents
# * **User** is anonymous
# * **Service** tracks analytics of pages
#     * Monthly visit stats
# * **Service** deletes expired pastes
# * **Service** has high availability

# #### Out of scope
# * **User** registers for an account
#     * **User** verifies email
# * **User** logs into a registered account
#     * **User** edits the document
# * **User** can set visibility
# * **User** can set the shortlink

# ### Constraints and assumptions
     
# * Traffic is not evenly distributed
# * Following a short link should be fast
# * Pastes are text only
# * Page view analytics do not need to be realtime
# * 10 million users
# * 10 million paste writes per month
# * 100 million paste reads per month
# * 10:1 read to write ratio

# Understand the problem, by creating a detailed step-by-step plan. Create additional tests, checks and evaluation at each step when applicable to help make excellent code implementation. You can use any package and any other packages you wish to install. Use best software design practices, and you can output large amounts of code at once."""},
                        ]
    


    # messages = [{"role": "user", "content": "What's the weather like in Boston?"}]
    # functions = [
    #     {
    #         "name": "get_current_weather",
    #         "description": "Get the current weather in a given location",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "location": {
    #                     "type": "string",
    #                     "description": "The city and state, e.g. San Francisco, CA",
    #                 },
    #                 "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
    #             },
    #             "required": ["location"],
    #         },
    #     }
    # ]
    prompt_tokens = 0
    completion_tokens = 0
    name = 'CLI ChatGPT'
    while True:
        num_tokens = num_tokens_consumed_by_chat_request(messages=messages)
        
        if not messages[-1]["role"] == "user":
            message = session.prompt(HTML(f"<b>[Token Capacity Used: {((num_tokens / max_tokens) * 100.0):.2f}% | Tokens remaining {max_tokens - num_tokens}] >>> </b>"))
            messages.append({"role": "user", "content": message})
        llm_config = get_llm_config(config, logger, name, rate_limiter)
        llm_config['messages'] = messages
        # llm_config['functions'] = functions
        # llm_config['function_call'] = 'auto'
        llm_config['temperature'] = 1.0
        llm_config['top_p'] = 1.0
        response = chat_completion_rl(**llm_config)
        message_response = response["choices"][0]["message"]
        usage_response = response["usage"]
        console.line()
        # console.print(Markdown(message_response["content"].strip()))
        print(message_response["content"].strip())
        console.line()
        messages.append(message_response)





if __name__ == "__main__":
    run()

# Save all this code to a file and provide file names.
# Are there any unit tests that we can run for verifying successful completion of step 1?


