import os
import re
import unittest
import tempfile
import shutil
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from pathlib import Path
from long_vars import extension_to_language
from llm_utils import embedding_rl
import pandas as pd
import shelve
import numpy as np
import ast
import shutil
import subprocess
from time import perf_counter
import json
from timeout_decorator import timeout

def cache_or_compute(variable_key, computation_function, *args, cache_file="project_cache"):
    """
    Generic function to cache or compute data.
    
    Parameters:
    - variable_key (str): The key associated with the variable to be stored or retrieved from the cache.
    - computation_function (function): The function to compute the data if it's not in the cache.
    - *args: Arguments for the computation_function.
    - cache_file (str): Path to the project-wide shelve cache.

    Returns:
    - result: The cached or computed data.
    """
    
    # Access the shelve database
    with shelve.open(cache_file) as db:
        # If the data associated with the variable_key is already in the cache
        if variable_key in db:
            return db[variable_key]
        
        # If the data isn't in the cache, compute it
        result = computation_function(*args)
        
        # Store the computed data in the cache
        db[variable_key] = result

    return result


# =================================================================================================
# Summarizer

def load_code_files_into_dict(folder_path, number_lines=False, file_extensions=None, skip_tests=False):
    root_path = Path(folder_path)
    code_files_dict = {}

    # Consider these as typical code or text file extensions
    # code_file_extensions = ['.py', '.c', '.cpp', '.h', '.java', '.js', '.ts', '.html', '.css', '.md', '.txt', '.xml']
    if file_extensions is None:
        code_file_extensions = ['.py', '.c', '.cpp', '.h', '.java', '.js', '.ts', '.html', '.css', '.txt', '.xml', '.sql']
    else:
        code_file_extensions = file_extensions

    for current_path, _, files in os.walk(root_path):
        # Skip the .git folder
        if ".git" in current_path:
            continue

        for file in files:
            if Path(file).suffix not in code_file_extensions:
                continue  # Skip non-code files

            if skip_tests and ('test' in file.lower() or 'test' in current_path.lower()):
                continue

            file_path = Path(current_path) / file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.read().split('\n')
                    if number_lines:
                        numbered_lines = [f"{idx + 1}: {line}" for idx, line in enumerate(lines)]
                    else:
                        numbered_lines = lines
                    code_files_dict[str(file_path.relative_to(root_path))] = numbered_lines
            except UnicodeDecodeError:
                # Skip non-UTF-8 encoded files
                continue
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return code_files_dict


def count_total_characters(data):
    total_chars = 0
    for content in data.values():
        # If content is a list of lines
        if isinstance(content, list):
            for line in content:
                total_chars += len(line)
        # If content is an empty string (e.g. non-text files)
        elif isinstance(content, str):
            total_chars += len(content)
    return total_chars

def count_key_characters(data):
    return sum(len(key) for key in data.keys())

def extract_file_names(s):
    file_name_pattern = r'([\w/]+\.ts)'
    matches = re.findall(file_name_pattern, s)
    matches = list(set(matches))
    return matches

def format_files_into_prompt_format(file_dict, unique_file_names=None, character_limit=14_000):
    """
    Generate a string output based on the given dictionary of files and an optional set of unique file names.
    
    Parameters:
    - file_dict: Dictionary with file names as keys and list of lines as values.
    - unique_file_names (optional): Set of unique file names to be extracted from the files dictionary.

    Returns:
    - A string representation in the specified format.
    """

    # If unique_file_names is not provided, process all file names in the dictionary
    if unique_file_names is None:
        unique_file_names = file_dict.keys()

    files_missed_out = []
    output = ""
    for file_name in unique_file_names:
        # Determine the language based on the file extension
        file_extension = file_name[file_name.rfind('.'):]
        lang = extension_to_language.get(file_extension, 'LANG')
        
        content = file_dict.get(file_name, [])
        additional_output = file_name + "\n```" + lang + "\n" + "\n".join(content) + "\n```\n\n"
        if (len(output) + len(additional_output)) < character_limit:
            output += file_name + "\n```" + lang + "\n" + "\n".join(content) + "\n```\n\n"
        else:
            files_missed_out.append(file_name)
    return output, files_missed_out

def remove_line_numbers(strings):
    # Regular expression pattern to match 'number: ' at the beginning of each string
    pattern = r'^\d+:\s'
    return [re.sub(pattern, '', s) for s in strings]

def add_line_numbers(strings):
    numbered_lines = [f"{idx + 1}: {line}" for idx, line in enumerate(strings)]
    return numbered_lines

def fix_line_spacings(strings):
    # Regular expression pattern to match 'number: ' at the beginning of each string
    lines = []
    for line in strings:
        leading_spaces = len(line) - len(line.lstrip(' '))
        leading_spaces = int(np.ceil(leading_spaces / 2) * 2)
        line = ' ' * leading_spaces + line.lstrip(' ')
        lines.append(line)
    return lines

def fix_indentation(lines: [str]) -> [str]:
    fixing_rounds = 0
    valid_python = False
    while not valid_python and fixing_rounds < 10:
        try:
            ast.parse('\n'.join(lines))
            valid_python = True
        except IndentationError as e:
            fixing_rounds += 1
            # Fix indentation
            prob_ln = e.args[1][1] - 1
            line = lines[prob_ln]
            prev_line = lines[prob_ln - 1]
            if prev_line == '':
                break
            leading_spaces = len(prev_line) - len(prev_line.lstrip(' '))
            leading_spaces += 2
            line = ' ' * leading_spaces + line.lstrip(' ')
            lines[prob_ln] = line
        except Exception as e:
            break
    return lines

# =================================================================================================
# Summarizer Using Embeddings

def embed_dataframe(df, batch_size = 16):
    """
    Embed 'code_raw' cells in the dataframe using the embedding_rl function.
    
    Parameters:
    - df (pd.DataFrame): Dataframe containing the 'code_raw' column to embed.

    Returns:
    - df_embedded (pd.DataFrame): Dataframe with an additional 'embeddings' column.
    """
    # Make sure 'code_raw' exists in dataframe
    if 'code_raw' not in df.columns:
        raise ValueError("The dataframe must contain a 'code_raw' column.")
    
    # Split the 'code_raw' column into batches of size 2048 or fewer
    n = len(df)
    code_batches = [df['code_raw'].iloc[i:i+batch_size].tolist() for i in range(0, n, batch_size)]
    
    # For each batch, get the embeddings using the embedding_rl function
    all_embeddings = []
    for batch in code_batches:
        embeddings = embedding_rl(batch)
        all_embeddings.extend(embeddings)

    # Add the embeddings back to the dataframe
    df['embeddings'] = all_embeddings

    return df

def embed_all_code_files(file_dict):
    df = pd.DataFrame([{'file_path': k, 'code': v} for k, v in file_dict.items()])
    df['code_raw'] = df['code'].apply(lambda x: '\n'.join(remove_line_numbers(x)))
    df = embed_dataframe(df)
    return df

# =========================================================================
# Write files out utility functions

def write_files_from_dict(file_dict, base_dir="./output"):
    """
    Writes files to a folder based on the given dictionary.
    
    :param file_dict: Dictionary with filenames as keys and lists of file content as values.
    :param base_dir: Base directory where files should be saved.
    """
    # Ensure base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Iterate through the file dictionary
    for file_path, lines in file_dict.items():
        # Construct the full path for the file
        full_path = os.path.join(base_dir, file_path)
        
        # Create the directories if they don't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        lines = fix_line_spacings(remove_line_numbers(lines))
        # Write content to the file
        with open(full_path, "w") as f:
            for line in lines:
                f.write(line + "\n")

# =========================================================================
# Misc


def write_files_from_dict(file_dict, base_dir="output"):
    """
    Writes files to a folder based on the given dictionary.
    
    :param file_dict: Dictionary with filenames as keys and lists of file content as values.
    :param base_dir: Base directory where files should be saved.
    """

    # If base directory exists, remove it
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

    # Ensure base directory is created again
    os.makedirs(base_dir)
    
    # Iterate through the file dictionary
    for file_path, lines in file_dict.items():
        # Construct the full path for the file
        full_path = os.path.join(base_dir, file_path)
        
        # Create the directories if they don't exist
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        lines = fix_line_spacings(remove_line_numbers(lines))
        # Write content to the file
        with open(full_path, "w") as f:
            for line in lines:
                f.write(line + "\n")

# =========================================================================
# Syntax checker

@timeout(60, timeout_exception=StopIteration)
def check_syntax(file_dict: dict):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        # Look for top level folders
        top_folders = list(set([file_name.split('/')[0] for file_name in file_dict.keys() if '/' in file_name]))
        top_modules = list(set([top_folder for top_folder in top_folders if f'{top_folder}/__init__.py' in file_dict.keys()]))
        top_modules_extra = list(set([file_name.split('/')[0] for file_name in file_dict.keys() if file_name.count('/') >= 2 and '.py' in file_name]))
        top_modules.extend(top_modules_extra)
        top_folder_with_code = [top_folder for top_folder in top_folders if (not f'{top_folder}/__init__.py' in file_dict.keys()) and (len([f for f in file_dict.keys() if top_folder in f and f.endswith('.py')]) >= 1)]
        top_code_files = [f for f in file_dict.keys() if f.endswith('.py') and not '/' in f]
        pylint_args = []
        pylint_args.extend(top_modules)
        pylint_args.extend([f'{f}/*.py' for f in top_folder_with_code])
        pylint_args.extend(top_code_files)
        command = ['python3', '-m',  'pylint', '--disable=all', '--enable=E', '--score=no']
        if len(pylint_args) == 0:
            # No python files found, therefore skipping
            return ''
        command.extend(pylint_args)
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True,
            cwd=tmpdirname)
        stderr = result.stderr
        stdout = result.stdout
    return stdout

def count_errors_in_syntax(syntax_output: str):
    pattern = r".+:\d+:\d+: [E]\d+: .+"
    errors = re.findall(pattern, syntax_output)
    return len(errors)

# =========================================================================
# PyTest
import xml.etree.ElementTree as ET

def parse_and_print_junit_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    testsuites = []
    for testsuite in root.findall('testsuite'):
        total_tests = int(testsuite.get("tests", 0))
        errors = int(testsuite.get("errors", 0))
        failures = int(testsuite.get("failures", 0))
        skipped = int(testsuite.get("skipped", 0))
        passed = total_tests - (errors + failures + skipped)

        results = {
            "total": total_tests,
            "passed": passed,
            "errors": errors,
            "failures": failures,
            "skipped": skipped
        }
        testsuites.append(results)
    return testsuites

@timeout(60, timeout_exception=StopIteration)
def check_pytest(file_dict: dict):
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
            if total_tests == total_passed:
                output = 'All tests passed.'
            else:
                output = f'Failed tests. Please check the output below. {stdout}'
        except FileNotFoundError as e:
            output = 'No tests found.'
        # print(stdout)
        # print(stderr)
        # print(results)
        # print('=====================')
    return output


class TestSummarizer(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    

    def test_group_chat_implementation(self):
        code_repository_folder_file_path = "./test_suite/mock_data/chatbot-ui/"

        # Assuming your agent's method to process and output code is named "process"
        output = load_code_files_into_dict(code_repository_folder_file_path)

        total_characters = count_total_characters(output)
        print(f"Total characters in the data structure: {total_characters}")

        total_key_characters = count_key_characters(output)
        print(f"Total characters in the dictionary keys: {total_key_characters}")
        print(f"Total characters in the dictionary values: {total_characters - total_key_characters}")

    def test_extract_file_names(self):
        string_content = """
To add this feature we need to consider both the frontend and backend parts of the implementation.

On the frontend, we'll have to:

1. Add the new button in the appropriate component file. As this is a chat feature, it seems likely that the required component would be located in the `components/` directory, but without viewing the contents it's hard to say for certain which file we should target. I suggest inspecting `components/Sidebar/index.ts` and `components/Buttons/SidebarActionButton/index.ts`. These file names suggest they might contain the code defining the chat UI and its buttons.

2. Once we've created our button, we'll need to bind an onClick event handler to it. This event handler will interact with `pages/api/chat.ts`.

On the backend:

1. We need to define the API route which will handle delete requests for chat message history. I suggest viewing the contents of `pages/api/chat.ts` to see if there is an existing endpoint we can adapt, or whether we need to define a new one.

May I proceed to view the contents of `components/Sidebar/index.ts`, `components/Buttons/SidebarActionButton/index.ts`, and `pages/api/chat.ts`?
"""
        files = extract_file_names(string_content)



# Create a Test Suite
class TestGenerateOutput(unittest.TestCase):

    def setUp(self):
        self.files = {
            'components/Sidebar/index.ts': ['import React from "react";', '...'],
            'components/Buttons/SidebarActionButton/index.ts': ['import React from "react";', '...'],
            'pages/api/chat.ts': ['import { NextApiRequest, NextApiResponse } from "next";', '...']
        }

    def test_all_files_returned(self):
        result = format_files_into_prompt_format(self.files)
        for file_name in self.files.keys():
            self.assertIn(file_name, result)

    def test_specific_files_returned(self):
        unique_files = {'pages/api/chat.ts'}
        result = format_files_into_prompt_format(self.files, unique_files)
        self.assertIn('pages/api/chat.ts', result)
        self.assertNotIn('components/Sidebar/index.ts', result)
        self.assertNotIn('components/Buttons/SidebarActionButton/index.ts', result)

class TestLoadCodeFilesIntoDictFormat(unittest.TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_temp_file(self, folder, filename, content):
        with open(Path(folder) / filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def test_line_format(self):
        # Create a sample file with multiple lines
        file_content = "Line1\nLine2\nLine3"
        self.create_temp_file(self.temp_dir.name, "sample.txt", file_content)

        result = load_code_files_into_dict(self.temp_dir.name)
        expected_result = [
            "1: Line1",
            "2: Line2",
            "3: Line3"
        ]
        self.assertIn("sample.txt", result)
        self.assertEqual(result["sample.txt"], expected_result)

    def test_line_format_large_file(self):
        # Test with a large file
        lines = [f"Line {i}" for i in range(1, 1001)]  # 1000 lines
        file_content = "\n".join(lines)
        self.create_temp_file(self.temp_dir.name, "large.txt", file_content)

        result = load_code_files_into_dict(self.temp_dir.name)
        self.assertIn("large.txt", result)

        # Ensure that the line format is correct for all lines
        for idx, line in enumerate(result["large.txt"], start=1):
            expected_line = f"{idx}: Line {idx}"
            self.assertEqual(line, expected_line)


# Unit test class
class TestRemoveLineNumbers(unittest.TestCase):
    def test_remove_line_numbers(self):
        # Test case 1
        input_strings = ['5: We appreciate your interest in contributing to our project.', '25: git clone https://github.com/mckaywrigley/chatbot-ui.git']
        expected_output = ['We appreciate your interest in contributing to our project.', 'git clone https://github.com/mckaywrigley/chatbot-ui.git']
        self.assertEqual(remove_line_numbers(input_strings), expected_output)

        # Test case 2: Test strings without line numbers and colons
        input_strings = ['Hello World!', 'Python is fun.']
        self.assertEqual(remove_line_numbers(input_strings), input_strings)

        # Test case 3: Test empty strings and strings with only line numbers and colons
        input_strings = ['5: ', '25:', '']
        expected_output = [' ', '', '']
        self.assertEqual(remove_line_numbers(input_strings), expected_output)

class TestFixLineSpacings(unittest.TestCase):
    def test_fix_line_spacings(self):
        # Test case 1
        input_strings = ['   def add_message(self, message):',
                         '    def __init__(self,chat_id,participants=None,messages=None):',
                         '        self.chat_id = chat_id',
                         '       self.messages.append(message)',
                         '  def add_message(self, message):',]
        expected_output = ['    def add_message(self, message):',
                         '    def __init__(self,chat_id,participants=None,messages=None):',
                         '        self.chat_id = chat_id',
                         '        self.messages.append(message)',
                         '  def add_message(self, message):',]
        self.assertEqual(fix_line_spacings(input_strings), expected_output)

class TestCheckSyntax(unittest.TestCase):

    def test_syntax_parser_on_file_dict_example_clean(self):
        file_dict = load_code_files_into_dict('repos/flask/examples/tutorial')
        syntax_output = check_syntax(file_dict)
        print(syntax_output)
        self.assertTrue(check_syntax({}), "Empty dictionary should be considered valid syntax")

    def test_syntax_parser_on_file_dict_example_errors(self):
        file_dict = load_code_files_into_dict('results/latest/run-20230922-044053_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-twitter_0_10-runs_log/whatsapp/1/LLMatic')
        syntax_output = check_syntax(file_dict)
        print(syntax_output)
        self.assertTrue(check_syntax({}), "Empty dictionary should be considered valid syntax")

    def test_syntax_parser_on_file_dict_giving_help_func(self):
        file_dict = {'requirements.txt': ['Flask', 'requests', 'sqlite3', 'pytest']}
        syntax_output = check_syntax(file_dict)
        print(syntax_output)
        self.assertTrue(check_syntax({}), "Empty dictionary should be considered valid syntax")

class TestPyTest(unittest.TestCase):

    def test_check_pytest_clean(self):
        file_dict = load_code_files_into_dict('repos/flask/examples/tutorial')
        syntax_output = check_pytest(file_dict)
        print(syntax_output)
        self.assertTrue(check_syntax({}), "Empty dictionary should be considered valid syntax")

    def test_check_pytest_errors(self):
        file_dict = load_code_files_into_dict('results/latest/run-20230922-044053_LLMatic-zero_shot_donnemartin-system-design-oop-whatsapp-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-twitter_0_10-runs_log/whatsapp/1/LLMatic')
        syntax_output = check_pytest(file_dict)
        print(syntax_output)
        self.assertTrue(check_syntax({}), "Empty dictionary should be considered valid syntax")


if __name__ == '__main__':
    # unittest.main()
    TestSummarizer().test_group_chat_implementation()
    # TestFixLineSpacings().test_fix_line_spacings()
    # TestCheckSyntax().test_syntax_parser_on_file_dict_example_clean()
    # TestCheckSyntax().test_syntax_parser_on_file_dict_example_errors()
    # TestCheckSyntax().test_syntax_parser_on_file_dict_giving_help_func()
    # TestPyTest().test_check_pytest_errors()
    # from utils.llm_tools import ProcessFunctionCall
    # # ProcessFunctionCall().test_process_function_call_and_return_message_empty()
    # ProcessFunctionCall().test_process_function_call_and_return_message_json_args_cut_short()
