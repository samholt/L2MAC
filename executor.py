import subprocess
import pickle
import base64
import traceback
import ast
import tempfile
import os
from summarizer_and_modifier import write_files_from_dict, load_code_files_into_dict, format_files_into_prompt_format
import json
from timeout_decorator import timeout
from llm_utils import num_tokens_from_messages
import numpy as np
from pathlib import Path

def extract_exception(output):
    """Try to extract exception information from the output. If found, raise it in the main process."""
    try:
        # Try to interpret the last line of output as a serialized exception
        exception_data = ast.literal_eval(output.splitlines()[-1])
        exception_message = exception_data.get('exception_message', '')
        exception_traceback = exception_data.get('exception_traceback', '')
        return exception_message, exception_traceback
    except (SyntaxError, ValueError):
        # If we can't interpret the output as a serialized exception, return None values
        return None, None

class Executor:
    def __init__(self, prepend_code_libraries="", variables=None):
        self.prepend_code_libraries = prepend_code_libraries
        if variables is None:
            self.variables = {}
        else:
            self.variables = variables

    def execute_user_code_lines(self, code_string):
        serialized_vars = base64.b64encode(pickle.dumps(self.variables)).decode('utf-8')
        lines = code_string.strip().split('\n')
        if lines:
            last_line = lines[-1].strip()
            if not (last_line.startswith("print(") or "=" in last_line or "import" in last_line or "#" in last_line):
                code_string += f"\nprint({last_line})"

        def auto_indent(code, spaces=4):
            indentation = ' ' * spaces
            return '\n'.join([indentation + line for line in code.split('\n')])

        full_code = f"""
import pickle
import base64
import traceback
import sys

# Deserialize variables
variables = pickle.loads(base64.b64decode('{serialized_vars}'.encode('utf-8')))
locals().update(variables)

try:
{auto_indent(self.prepend_code_libraries)}
{auto_indent(code_string)}
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
    sys.stderr.write(str({{
        'exception_message': str(exc_value),
        'exception_traceback': formatted_traceback
    }}))
    raise SystemExit(1)
"""
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.py') as temp:
            temp.write(full_code)
            temp_file_name = temp.name
            
        try:
            result = subprocess.run(
                ["python3", temp_file_name], 
                capture_output=True, 
                text=True)
        finally:
            os.remove(temp_file_name)
        if result.returncode != 0:
            if "SyntaxError" in result.stderr:
                raise SyntaxError(f"Syntax error in user code:\n{result.stderr.strip()}")
            else:
                exception_message, exception_traceback = extract_exception(result.stderr)
            raise Exception(f"{result.stdout}\nUser code exception: {exception_message}\n\n{exception_traceback}")
        else:
            captured_output = result.stdout.strip()
            return captured_output

@timeout(60, timeout_exception=StopIteration)
def pytest_code_base_with_xml(file_dict, files_to_test=None):
    from summarizer_and_modifier import parse_and_print_junit_xml
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        # write_files_from_dict(file_dict)
        command = ['python3', '-m',  'pytest', '--junitxml=result_pytest.xml']
        if files_to_test is not None:
            command.extend(files_to_test)
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
    return output

@timeout(60, timeout_exception=StopIteration)
def pytest_code_base(file_dict, files_to_test=None):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        # write_files_from_dict(file_dict)
        command = ['python3', '-m',  'pytest']
        if files_to_test is not None:
            command.extend(files_to_test)
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True,
            cwd=tmpdirname)
        captured_output = result.stdout.strip()
        print(captured_output)
        print('')
    return captured_output

@timeout(20, timeout_exception=StopIteration)
def python_run_code_base(file_dict, file, arguments=[]):
    with tempfile.TemporaryDirectory() as tmpdirname:
        write_files_from_dict(file_dict, tmpdirname)
        command = ["python3", file]
        if arguments is not None:
            command.extend(arguments)
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True,
            cwd=tmpdirname)
        if result.returncode != 0:
            captured_output = result.stderr.strip()
        else:
            captured_output = result.stdout.strip()
    return captured_output
    
import unittest

class TestExecutor(unittest.TestCase):

    def setUp(self):
        self.executor = Executor(variables={'a': 1, 'b': 2})

    def test_basic_execution(self):
        result = self.executor.execute_user_code_lines("print(a + b)")
        self.assertEqual(result.strip(), '3')

    def test_exception_handling(self):
        with self.assertRaises(Exception) as context:
            self.executor.execute_user_code_lines("print(undeclared_variable)")
        5
        self.assertIn("User code exception:", str(context.exception))
        self.assertIn("name 'undeclared_variable' is not defined", str(context.exception))

    def test_syntax_error(self):
        with self.assertRaises(Exception) as context:
            self.executor.execute_user_code_lines("print(")  # Unmatched parenthesis will raise a SyntaxError

        self.assertIn('SyntaxError', context.exception.args[0])  
        # self.assertIn('unexpected EOF while parsing', context.exception.args[0])

    def test_pytest_code_base(self):
        from examples.chat_app_2 import file_dict
        result = pytest_code_base(file_dict)
        self.assertTrue(result.strip())

    def test_python_run_code_base_error_out(self):
        from examples.parking_executing_main import data
        data = json.loads(data)
        result = python_run_code_base(data['file_dict'], 'main.py')
        self.assertTrue('SyntaxError' in result)

    def test_python_run_code_base_normal_out(self):
        from examples.parking_executing_main import data
        data = json.loads(data)
        file_dict = data['file_dict']
        file_dict['main.py'][20] = "21:     print(f\"Parking lot availability: {'Available' if parking_lot.is_available() else 'Full'}\")"
        file_dict['main.py'][30] = "31:     print(f\"Parking lot availability: {'Available' if parking_lot.is_available() else 'Full'}\")"
        result = python_run_code_base(data['file_dict'], 'main.py')
        self.assertTrue('SyntaxError' not in result)

    def test_pytest_too_much_error_out(self):
        file_dict = load_code_files_into_dict('results/run-20230922-234515_LLMatic_donnemartin-system-design-oop-whatsapp_0_10-runs_log/whatsapp/0/LLMatic')
        # 4000 tokens max
        output = format_files_into_prompt_format(file_dict, list(file_dict.keys()))
        resized_output = output
        print(num_tokens_from_messages([{'content': resized_output}]))
        print(resized_output)
        output = pytest_code_base(file_dict)
        resized_output = output[:6000]
        print(num_tokens_from_messages([{'content': resized_output}]))
        print(resized_output)
        # self.assertTrue(check_syntax({}), "Empty dictionary should be considered valid syntax")

    # def test_exception_handling_missing_library(self):
    #     try:
    #         self.executor.execute_user_code_lines("np.array([1, 2, 3])")
    #     except Exception as e:
    #         print(e)
    #         print(e.args[0])
    #         print(e.args)
    #         print(e.__traceback__)
    #         print('')
    #     print('')
    #     with self.assertRaises(Exception) as context:
    #         self.executor.execute_user_code_lines("print(undeclared_variable)")
        
    #     self.assertIn("User code exception:", str(context.exception))
    #     self.assertIn("name 'undeclared_variable' is not defined", str(context.exception))

    def test_last_expression_printed(self):
        result = self.executor.execute_user_code_lines("""
print(a)
a + b
""")
        self.assertEqual(result.strip().split("\n"), ['1', '3'])


    def test_multiple_prints_and_expression(self):
        result = self.executor.execute_user_code_lines("""
print(a)
print(b)
a + b
""")
        self.assertEqual(result.strip().split("\n"), ['1', '2', '3'])

    def test_last_expression_skipped_if_not_valid(self):
        result = self.executor.execute_user_code_lines("""
print(a)
print(b)
a = a + b
""")
        self.assertEqual(result.strip().split("\n"), ['1', '2'])

    def test_variables_injected(self):
        result = self.executor.execute_user_code_lines("print(a)")
        self.assertEqual(result.strip(), '1')

        result = self.executor.execute_user_code_lines("print(b)")
        self.assertEqual(result.strip(), '2')

if __name__ == '__main__':
    # unittest.main()

    TestExecutor().test_pytest_too_much_error_out()

    # a = TestExecutor()
    # a.setUp()
    # a.test_python_run_code_base_normal_out()
    # # a.test_exception_handling()
    # # a.test_exception_handling_missing_library()
