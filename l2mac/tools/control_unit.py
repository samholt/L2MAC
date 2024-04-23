import json
from typing import List

from l2mac.tools.code_analysis import (
    check_pytest_with_timeout,
    check_syntax_with_timeout,
    count_errors_in_syntax,
)


def provide_detailed_sub_task_steps_for_sub_agents(steps: List[str] = []):
    return steps


def check_sub_task_step_complete(file_dict: dict = {}, enable_tests=True):
    # Run tests
    # Syntax check
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
            # if len(new_output) > 5000:
            #     new_output = new_output[:5000]
            #     new_output = new_output + '\nRest of output was trimmed.'
            output = {
                "status": "error",
                "message": "Failed validation checks, sub task step is not yet complete. Test run results: \n"
                + new_output,
            }
        else:
            new_output = syntax_results.strip()
            # if len(new_output) > 5000:
            #     new_output = new_output[:5000]
            #     new_output = new_output + '\nRest of output was trimmed.'
            output = {
                "status": "error",
                "message": "Failed validation checks, sub task step is not yet complete. Code failed syntax checks: \n"
                + new_output
                + "\n You must fix this code by writing code to complete this sub task step. If a test is failing the error could be the code, or the test is incorrect, so feel free to modify and change the tests when they are incorrect, to make all tests pass.",
            }
    return json.dumps(output)
