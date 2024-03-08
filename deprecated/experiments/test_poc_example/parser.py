import ast
import os

def extract_function_info(node):
    if isinstance(node, ast.FunctionDef):
        return {
            "name": node.name,
            "parameters": [param.arg for param in node.args.args],
            "docstring": ast.get_docstring(node),
            "lineno": node.lineno,
        }
    return None

def parse_codebase(folder_path):
    code_info = []
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".py"):
                filepath = os.path.join(root, filename)
                with open(filepath, "r") as file:
                    code = file.read()
                try:
                    parsed = ast.parse(code)
                except SyntaxError:
                    print(f"Syntax error in {filepath}")
                    continue
                functions = [
                    extract_function_info(node) for node in ast.walk(parsed)
                ]
                functions = [f for f in functions if f is not None]
                code_info.extend(functions)
    return code_info

def main():
    codebase_folder = "./experiments/test_poc_example/"
    code_info = parse_codebase(codebase_folder)

    for function in code_info:
        print(f"Function: {function['name']}")
        print(f"Parameters: {', '.join(function['parameters'])}")
        print(f"Docstring: {function['docstring']}")
        print(f"Location: Line {function['lineno']}\n")


def print_file_with_line_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # main()
    file_path = './experiments/test_poc_example/room_occ/a1.py'  # Replace this with the path to the file you want to read
    print_file_with_line_numbers(file_path)