"""
This module provides functions to check the completion status of sub-task steps
by running syntax checks and tests on the provided code files.

Functions:
- provide_detailed_sub_task_steps_for_sub_agents(steps: List[str]) -> List[str]:
  Returns the provided list of steps for sub-agents.

- check_sub_task_step_complete(file_dict: dict, enable_tests=True) -> str:
  Checks if the sub-task step is complete by running syntax checks and tests
  on the provided code files. Returns a JSON string with the status and message
  indicating whether the task step is complete or not.
"""
import json
from typing import List

from l2mac.tools.code_analysis import (
    check_pytest_with_timeout,
    check_syntax_with_timeout,
    count_errors_in_syntax,
)


def provide_detailed_sub_task_steps_for_sub_agents(steps: List[str]):
  return steps


def check_sub_task_step_complete(file_dict: dict, enable_tests=True):
  # Run tests & Syntax checks
  if not enable_tests:
    output = {"status": "TASK_STEP_COMPLETE", "message": "All tests passed"}
    return json.dumps(output)
  syntax_results = check_syntax_with_timeout(file_dict)
  if "Manual tests passed" in syntax_results:
    syntax_error_count = 0
  else:
    syntax_error_count = count_errors_in_syntax(syntax_results)
  test_results = check_pytest_with_timeout(file_dict)
  if "Manual tests passed" in test_results:
    test_results = "All tests passed"
  elif "No tests found" in test_results:
    test_results = "All tests passed"
  if "All tests passed" in test_results and syntax_error_count == 0:
    output = {"status": "TASK_STEP_COMPLETE", "message": "All tests passed"}
  else:
    if "All tests passed" not in test_results:
      new_output = test_results.strip() + "\n" + syntax_results.strip()
      output = {
          "status":
          "error",
          "message":
          "Failed validation checks, sub task step is not yet complete. "
          "Test run results: \n"
          + new_output,
      }
    else:
      new_output = syntax_results.strip()
      output = {
          "status":
          "error",
          "message":
          "Failed validation checks, sub task step is not yet complete. "
          "Code failed syntax checks: \n"
          + new_output +
          "\n You must fix this code by writing code to complete this sub task "
          "step. If a test is failing the error could be the code, or the test "
          "is incorrect, so feel free to modify and change the tests when they "
          "are incorrect, to make all tests pass.",
      }
  return json.dumps(output)
