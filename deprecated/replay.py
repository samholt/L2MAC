import pandas as pd
import numpy as np
import torch
import random
from utils.results_utils import *
from time import time
import shelve
from enum import Enum
seed_all(0)
# from llm_utils import pretty_print_chat_messages
def pretty_print_chat_messages(messages):
    COLORS = {
        "system": "\033[95m",      # Light Magenta
        "user": "\033[94m",       # Light Blue
        "assistant": "\033[92m"   # Light Green
    }
    ROLE_MAP = {
        "system": "green",      # Light Magenta
        "user": "blue",       # Light Blue
        "assistant": "red"   # Light Green
    }
    
    for msg in messages:
        role = msg['role']
        color = COLORS.get(role, COLORS["system"])  # Default to system color if role not found
        formatted_role = role.capitalize()
        content = msg['content']
        # print(f"{color}[{formatted_role}] {content}\033[0m")  # Reset color at the end
        print("\n\n\color{" + ROLE_MAP[role] + "}\n\\textbf{[" + formatted_role + "]}\n\\begin{lstlisting}\n" + content + "\n\end{lstlisting}")

LOG_PATH = './logs/run-20230829-034759_relentless-zero_shot_data-science-diabetes_0_3-runs_log.txt'
with open(LOG_PATH) as f:
    lines = f.readlines()
pd_l = []
for line in tqdm(lines):
    if "'messages': [{'role':" in line:
        result_dict = line.split("'messages':")[1].strip()
        result_dict = result_dict.split("}]}")[0].strip() + '}]'
        result_dict = ast.literal_eval(result_dict)
        pretty_print_chat_messages(result_dict)
        print('=============================\n=============================\n')
        # except:
        #     pass
