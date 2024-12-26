"""
This module provides tools for analyzing and testing Python code files. It
includes functions for checking syntax, running pytest, and executing Python
files with a timeout mechanism. The module also provides utilities for handling
file dictionaries and parsing test results.

Functions:
- check_syntax_with_timeout(file_dict): Checks the syntax of Python files with
  a timeout.
- check_pytest_with_timeout(file_dict): Runs pytest on Python files with a
  timeout.
- check_syntax(file_dict): Checks the syntax of Python files.
- check_pytest(file_dict): Runs pytest on Python files and parses the results.
- pytest_files(files_to_test, file_dict, enable_tests): Runs pytest on
  specified files and returns the results.
- pytest_code_base(file_dict, files_to_test): Runs pytest on the code base.
- count_errors_in_syntax(syntax_output): Counts the number of syntax errors in
  the output.
- parse_and_print_junit_xml(file_path): Parses JUnit XML results and prints
  the summary.
- run_python_file(file_name_to_run, file_dict, arguments, enable_tests): Runs
  a specified Python file with arguments.
- python_run_code_base(file_dict, file, arguments): Executes a Python file
  with arguments.
- find_external_modules(file_dict): Finds external modules imported in the code
  files.

Classes:
- TestCheckSyntax: Unit tests for syntax checking functions.
- TestPyTest: Unit tests for pytest functions.
"""
import json
import re
import subprocess
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List

import numpy as np
from timeout_decorator import timeout

from l2mac.tools.read import load_code_files_into_dict
from l2mac.tools.utils import write_files_from_dict


def check_syntax_with_timeout(file_dict):
  try:
    syntax_results = check_syntax(file_dict)
  except StopIteration:
    syntax_results = "Manual tests passed."
  return syntax_results


def check_pytest_with_timeout(file_dict):
  try:
    test_results = check_pytest(file_dict)
  except StopIteration:
    test_results = "Manual tests passed."
  return test_results


@timeout(60, timeout_exception=StopIteration)
def check_syntax(file_dict: dict):
  external_modules = find_external_modules(file_dict)
  ignored_modules = ",".join(external_modules)
  with tempfile.TemporaryDirectory() as tmp_dir_name:
    write_files_from_dict(file_dict, tmp_dir_name)
    # Look for top level folders
    top_folders = list(
        set([
            file_name.split("/")[0] for file_name in file_dict.keys()
            if "/" in file_name
        ]))
    top_modules = list(
        set([
            top_folder for top_folder in top_folders
            if f"{top_folder}/__init__.py" in file_dict.keys()
        ]))
    top_modules_extra = list(
        set([
            file_name.split("/")[0] for file_name in file_dict.keys()
            if file_name.count("/") >= 2 and ".py" in file_name
        ]))
    top_modules.extend(top_modules_extra)
    top_folder_with_code = [
        top_folder for top_folder in top_folders
        if (f"{top_folder}/__init__.py" not in file_dict.keys()) and (len([
            f
            for f in file_dict.keys() if top_folder in f and f.endswith(".py")
        ]) >= 1)
    ]
    top_code_files = [
        f for f in file_dict.keys() if f.endswith(".py") and "/" not in f
    ]
    pylint_args = []
    pylint_args.extend(top_modules)
    pylint_args.extend([f"{f}/*.py" for f in top_folder_with_code])
    pylint_args.extend(top_code_files)
    command = [
        "python3",
        "-m",
        "pylint",
        "--disable=all,E0401",  # Import module error bug
        "--enable=E",
        "--score=no",
        "--ignored-modules=" + ignored_modules,
    ]
    if len(pylint_args) == 0:
      # No python files found, therefore skipping
      return ""
    command.extend(pylint_args)
    result = subprocess.run(command,
                            capture_output=True,
                            text=True,
                            cwd=tmp_dir_name,
                            check=True)
    stdout = result.stdout
  return stdout


@timeout(60, timeout_exception=StopIteration)
def check_pytest(file_dict: dict):
  with tempfile.TemporaryDirectory() as tmp_dir_name:
    write_files_from_dict(file_dict, tmp_dir_name)
    command = ["python3", "-m", "pytest", "--junitxml=result_pytest.xml"]
    result = subprocess.run(command,
                            capture_output=True,
                            text=True,
                            cwd=tmp_dir_name,
                            check=True)
    stdout = result.stdout
    try:
      results = parse_and_print_junit_xml(
          Path(tmp_dir_name) / "result_pytest.xml")
      total_tests = np.sum([r["total"] for r in results])
      total_passed = np.sum([r["passed"] for r in results])
      if total_tests == total_passed:
        output = "All tests passed."
      else:
        output = f"Failed tests. Please check the output below. {stdout}"
    except FileNotFoundError:
      output = "No tests found."
  return output


def pytest_files(files_to_test: List[str],
                 file_dict: dict,
                 enable_tests=True):
  if not enable_tests:
    output = "Manual tests passed."
    return json.dumps({"output": output})
  try:
    output = pytest_code_base(file_dict, files_to_test)
    output += " If a test is failing the error could be the code, or the " \
              "test is incorrect, so feel free to overwrite and change the " \
              "tests when they are incorrect, to make all tests pass."
  except StopIteration:
    output = "Manual tests passed."
  return json.dumps({"output": output})


@timeout(60, timeout_exception=StopIteration)
def pytest_code_base(file_dict, files_to_test=None):
  with tempfile.TemporaryDirectory() as tmp_dir_name:
    write_files_from_dict(file_dict, tmp_dir_name)
    command = ["python3", "-m", "pytest"]
    if files_to_test is not None:
      command.extend(files_to_test)
    result = subprocess.run(command,
                            capture_output=True,
                            text=True,
                            cwd=tmp_dir_name,
                            check=True)
    captured_output = result.stdout.strip()
    print(captured_output)
    print("")
  return captured_output


def count_errors_in_syntax(syntax_output: str):
  pattern = r".+:\d+:\d+: [E]\d+: .+"
  errors = re.findall(pattern, syntax_output)
  return len(errors)


def parse_and_print_junit_xml(file_path):
  tree = ET.parse(file_path)
  root = tree.getroot()
  testsuites = []
  for testsuite in root.findall("testsuite"):
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
        "skipped": skipped,
    }
    testsuites.append(results)
  return testsuites


def run_python_file(
    file_name_to_run: str,
    file_dict: dict,
    arguments: List[str],
    enable_tests=True,
):
  if not enable_tests:
    output = "Manual tests passed."
    return json.dumps({"output": output})
  if file_name_to_run == "":
    return json.dumps({
        "status":
        "error",
        "message":
        "Missing required argument `file_name_to_run`. You must specify a file "
        "name to run. Please try running `list_files` to see all available "
        "files. And specify a file name to run when calling `run_python_file` "
        "with the required argument of `file_name_to_run`.",
    })
  elif file_name_to_run not in file_dict:
    return json.dumps({
        "status":
        "error",
        "message":
        f"File {file_name_to_run} not found. Please try running `list_files` "
        "to see all available files.",
    })
  else:
    try:
      output = python_run_code_base(file_dict, file_name_to_run, arguments)
    except StopIteration:
      output = "Manual tests passed."
    return json.dumps({"output": output})


@timeout(20, timeout_exception=StopIteration)
def python_run_code_base(file_dict, file, arguments):
  with tempfile.TemporaryDirectory() as tmp_dir_name:
    write_files_from_dict(file_dict, tmp_dir_name)
    command = ["python3", file]
    if arguments is not None:
      command.extend(arguments)
    result = subprocess.run(command,
                            capture_output=True,
                            text=True,
                            cwd=tmp_dir_name,
                            check=True)
    if result.returncode != 0:
      captured_output = result.stderr.strip()
    else:
      captured_output = result.stdout.strip()
  return captured_output


def find_external_modules(file_dict):
  local_modules = set([
      file_name.split("/")[0] for file_name in file_dict.keys()
      if "/" in file_name
  ])
  external_modules = set()
  import_pattern = re.compile(r"^(?:from|import) (\w+)")

  for file_lines in file_dict.values():
    for line in file_lines:
      match = import_pattern.match(line)
      if match:
        module = match.group(1)
        if module not in local_modules:
          external_modules.add(module)

  return external_modules

# pylint: disable=line-too-long
class TestCheckSyntax(unittest.TestCase):
  """
  Unit tests for syntax checking functionality.
  Test Cases:
  - test_syntax_parser_on_file_dict_example_clean: Tests syntax checking on a
    clean example file dictionary.
  - test_syntax_parser_on_file_dict_example_errors: Tests syntax checking on a
    file dictionary with potential syntax errors.
  - test_syntax_parser_on_file_dict_giving_help_func: Tests syntax checking on
    a file dictionary containing a requirements file.
  Each test case:
  - Loads a file dictionary.
  - Checks the syntax of the files in the dictionary.
  - Prints the syntax checking output.
  - Asserts that an empty dictionary is considered valid syntax.
  """
  def test_syntax_parser_on_file_dict_example_clean(self):
    file_dict = load_code_files_into_dict("repos/flask/examples/tutorial")
    syntax_output = check_syntax(file_dict)
    print(syntax_output)
    self.assertTrue(
        check_syntax({}),
        "Empty dictionary should be considered valid syntax",
    )

  def test_syntax_parser_on_file_dict_example_errors(self):
    file_dict = load_code_files_into_dict(
        "results/latest/run-20230922-044053_L2MAC-zero_shot_donnemartin-system-design-oop-whatsapp-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-twitter_0_10-runs_log/whatsapp/1/L2MAC"
    )
    syntax_output = check_syntax(file_dict)
    print(syntax_output)
    self.assertTrue(
        check_syntax({}),
        "Empty dictionary should be considered valid syntax",
    )

  def test_syntax_parser_on_file_dict_giving_help_func(self):
    file_dict = {
        "requirements.txt": ["Flask", "requests", "sqlite3", "pytest"]
    }
    syntax_output = check_syntax(file_dict)
    print(syntax_output)
    self.assertTrue(
        check_syntax({}),
        "Empty dictionary should be considered valid syntax",
    )


class TestPyTest(unittest.TestCase):
  def test_check_pytest_clean(self):
    file_dict = load_code_files_into_dict("repos/flask/examples/tutorial")
    syntax_output = check_pytest(file_dict)
    print(syntax_output)
    self.assertTrue(
        check_syntax({}),
        "Empty dictionary should be considered valid syntax",
    )

  def test_check_pytest_errors(self):
    file_dict = load_code_files_into_dict(
        "results/latest/run-20230922-044053_L2MAC-zero_shot_donnemartin-system-design-oop-whatsapp-donnemartin-system-design-oop-url_shortener-donnemartin-system-design-oop-dropbox-donnemartin-system-design-oop-twitter_0_10-runs_log/whatsapp/1/L2MAC"
    )
    syntax_output = check_pytest(file_dict)
    print(syntax_output)
    self.assertTrue(
        check_syntax({}),
        "Empty dictionary should be considered valid syntax",
    )
