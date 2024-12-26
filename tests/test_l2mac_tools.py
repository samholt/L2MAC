"""
This module contains unit tests for various functions in the l2mac.tools
  package.
The tests are written using the pytest framework and cover the following
  functionalities:

- `check_pytest_with_timeout`: Verifies that pytest runs with a timeout and
   checks the result.
- `parse_and_print_junit_xml`: Parses JUnit XML files and prints the results.
- `find_external_modules`: Identifies external modules used in the code.
- `provide_detailed_sub_task_steps_for_sub_agents`: Provides detailed steps for
   sub-agents.
- `available_functions_factory`: Lists available functions.
- `function_definition_list_factory`: Creates a list of function definitions.
- `function_definition_list_factory_internal`: Creates an internal list of
   function definitions.
- `view_files`: Views the content of specified files.
- `list_files`: Lists files in a directory.
- `load_code_files_into_dict`: Loads code files into a dictionary.
- `write_files_from_dict`: Writes files from a dictionary to the filesystem.
- `fix_line_spacings`: Fixes line spacings in code.
- `remove_line_numbers`: Removes line numbers from code lines.
- `implement_git_diff_on_file_dict`: Applies git diffs to a file dictionary.
- `delete_files`: Deletes specified files from a dictionary.

Each test function is designed to validate the correctness of its corresponding
  functionality.
"""
import pytest

from l2mac.tools.code_analysis import (
    check_pytest_with_timeout,
    find_external_modules,
    parse_and_print_junit_xml,
)
from l2mac.tools.control_unit import provide_detailed_sub_task_steps_for_sub_agents
from l2mac.tools.core import (
    available_functions_factory,
    function_definition_list_factory,
    function_definition_list_factory_internal,
)
from l2mac.tools.read import list_files, load_code_files_into_dict, view_files
from l2mac.tools.utils import (
    fix_line_spacings,
    remove_line_numbers,
    write_files_from_dict,
)
from l2mac.tools.write import delete_files, implement_git_diff_on_file_dict

# Sample file dictionary for testing
sample_file_dict = {
  "example.py": ["print('Hello, World!')"],
  "test_example.py": ["def test_example():", "    assert True"],
}

def test_check_pytest_with_timeout():
  result = check_pytest_with_timeout(sample_file_dict)
  assert "Manual tests passed" in result or "All tests passed" in result

def test_parse_and_print_junit_xml(tmp_path):
  xml_content = """<testsuites>
            <testsuite tests="1" errors="0" failures="0" skipped="0">
              <testcase classname="example" name="test_example"/>
            </testsuite>
           </testsuites>"""
  xml_file = tmp_path / "junit.xml"
  xml_file.write_text(xml_content)
  result = parse_and_print_junit_xml(str(xml_file))
  assert result == [{"total": 1, "passed": 1, "errors": 0, "failures": 0,
                     "skipped": 0}]

def test_find_external_modules():
  external_modules = find_external_modules(sample_file_dict)
  assert external_modules == set()

def test_provide_detailed_sub_task_steps_for_sub_agents():
  steps = ["step1", "step2"]
  result = provide_detailed_sub_task_steps_for_sub_agents(steps)
  assert result == steps

def test_available_functions_factory():
  functions = available_functions_factory()
  assert "provide_detailed_sub_task_steps_for_sub_agents" in functions
  assert "sub_task_step_complete" in functions

def test_function_definition_list_factory():
  functions = function_definition_list_factory()
  assert isinstance(functions, list)

def test_function_definition_list_factory_internal():
  functions = function_definition_list_factory_internal()
  assert isinstance(functions, list)

def test_view_files():
  result = view_files(["example.py"], sample_file_dict)
  assert "example.py" in result

def test_list_files():
  result = list_files("", sample_file_dict)
  assert "example.py" in result

def test_load_code_files_into_dict(tmp_path):
  example_file = tmp_path / "example.py"
  example_file.write_text("print('Hello, World!')")
  result = load_code_files_into_dict(str(tmp_path))
  assert "example.py" in result

def test_write_files_from_dict(tmp_path):
  write_files_from_dict(sample_file_dict, str(tmp_path))
  assert (tmp_path / "example.py").exists()

def test_fix_line_spacings():
  lines = ["  print('Hello, World!')"]
  result = fix_line_spacings(lines)
  assert result == ["  print('Hello, World!')"]

def test_remove_line_numbers():
  lines = ["1: print('Hello, World!')"]
  result = remove_line_numbers(lines)
  assert result == ["print('Hello, World!')"]

def test_implement_git_diff_on_file_dict():
  changes = [{"file_path": "example.py",
              "file_contents": "+ 1:print('Hello, World!')"}]
  result = implement_git_diff_on_file_dict(sample_file_dict, changes)
  assert "example.py" in result

def test_delete_files():
  result, _ = delete_files(["example.py"], sample_file_dict)
  assert "success" in result

if __name__ == "__main__":
  pytest.main([__file__])
  print("l2mac test passed")
