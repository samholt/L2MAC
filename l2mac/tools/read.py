"""
This module provides utilities for reading and formatting code files into a 
specific prompt format, listing available files, and loading code files into 
a dictionary. It includes functions for viewing files, listing files, 
formatting files into a prompt format, and loading code files into a dictionary 
with optional line numbering and file extension filtering. Additionally, it 
contains a mapping of file extensions to programming languages and a unit test 
class for testing the formatting function.

Functions:
- view_files: Returns a JSON response with the content of specified files or 
  an error message if files are not found.
- list_files: Returns a JSON response with a list of available files.
- format_files_into_prompt_format: Formats the content of specified files into 
  a string representation with language-specific code blocks.
- load_code_files_into_dict: Loads code files from a specified folder into a 
  dictionary with optional line numbering and file extension filtering.

Classes:
- TestGenerateOutput: Unit test class for testing the
  format_files_into_prompt_format function.

Variables:
- extension_to_language: Dictionary mapping file extensions to programming 
  languages.
"""
import json
import os
import unittest
from pathlib import Path
from typing import List


def view_files(files: List[str],
               file_dict: dict,
               enable_tests=True): # pylint: disable=unused-argument
  files_not_found = []
  for f in files:
    if f not in file_dict:
      files_not_found.append(f)
  if len(files_not_found) > 0:
    return json.dumps({
        "status":
        "error",
        "message":
        f"Files {files_not_found} not found. Please try running `list_files` "
        "to see all available files.",
    })
  output, files_missed_out = format_files_into_prompt_format(
      file_dict=file_dict, unique_file_names=files)
  if len(files_missed_out) > 0:
    response = {
        "files":
        output,
        "status":
        "error",
        "message":
        f'''Due to the character limit of a response, the following files were 
        not included in the response {", ".join(files_missed_out)}. Please 
        try viewing less files at a time.''',
    }
  else:
    response = {"files": output}
  return json.dumps(response)


def list_files(folder_path: str, file_dict: dict, enable_tests=True): # pylint: disable=unused-argument
  return json.dumps({"files": list(file_dict.keys())})


def format_files_into_prompt_format(file_dict,
                                    unique_file_names=None,
                                    character_limit=14_000):
  """
    Generate a string output based on the given dictionary of files and an
    optional set of unique file names.

    Parameters:
    - file_dict: Dictionary with file names as keys and list of lines as values.
    - unique_file_names (optional): Set of unique file names to be extracted
    from the files dictionary.

    Returns:
    - A string representation in the specified format.
    """

  # If unique_file_names is not provided, process all file names in the
  # dictionary
  if unique_file_names is None:
    unique_file_names = file_dict.keys()

  files_missed_out = []
  output = ""
  for file_name in unique_file_names:
    # Determine the language based on the file extension
    file_extension = file_name[file_name.rfind("."):]
    lang = extension_to_language.get(file_extension, "LANG")

    content = file_dict.get(file_name, [])
    additional_output = (file_name + "\n```" + lang + "\n" +
                         "\n".join(content) + "\n```\n\n")
    if (len(output) + len(additional_output)) < character_limit:
      output += (file_name + "\n```" + lang + "\n" + "\n".join(content) +
                 "\n```\n\n")
    else:
      files_missed_out.append(file_name)
  return output, files_missed_out


def load_code_files_into_dict(folder_path,
                              number_lines=False,
                              file_extensions=None,
                              skip_tests=False):
  root_path = Path(folder_path)
  code_files_dict = {}

  # Consider these as typical code or text file extensions
  # code_file_extensions = ['.py', '.c', '.cpp', '.h', '.java', '.js', '.ts',
  # '.html', '.css', '.md', '.txt', '.xml']
  if file_extensions is None:
    code_file_extensions = [
        ".py",
        ".c",
        ".cpp",
        ".h",
        ".java",
        ".js",
        ".ts",
        ".html",
        ".css",
        ".txt",
        ".xml",
        ".sql",
    ]
  else:
    code_file_extensions = file_extensions

  for current_path, _, files in os.walk(root_path):
    # Skip the .git folder
    if ".git" in current_path:
      continue

    for file in files:
      if Path(file).suffix not in code_file_extensions:
        continue  # Skip non-code files

      if skip_tests and ("test" in file.lower()
                         or "test" in current_path.lower()):
        continue

      file_path = Path(current_path) / file
      try:
        with open(file_path, "r", encoding="utf-8") as f:
          lines = f.read().split("\n")
          if number_lines:
            numbered_lines = [
                f"{idx + 1}: {line}" for idx, line in enumerate(lines)
            ]
          else:
            numbered_lines = lines
          code_files_dict[str(
              file_path.relative_to(root_path))] = numbered_lines
      except UnicodeDecodeError:
        # Skip non-UTF-8 encoded files
        continue
      except (IOError, OSError) as e:
        print(f"Error reading {file_path}: {e}")

  return code_files_dict


class TestGenerateOutput(unittest.TestCase):
  """
  Unit tests for the format_files_into_prompt_format function.

  TestGenerateOutput is a test case class that contains unit tests to verify
    the behavior of the 
  format_files_into_prompt_format function. It includes the following tests:

  - setUp: Initializes a dictionary of file paths and their contents to be used
    in the tests.
  - test_all_files_returned: Verifies that all file names in the input
    dictionary are present in the output.
  - test_specific_files_returned: Verifies that only the specified unique file
    names are present in the output, and other file names are not included.

  Methods:
  - setUp: Sets up the initial conditions for the tests.
  - test_all_files_returned: Tests that all file names are returned in the
    output.
  - test_specific_files_returned: Tests that only specific file names are
    returned in the output.
  """
  def setUp(self):
    self.files = {
        "components/Sidebar/index.ts": [
            'import React from "react";',
            "...",
        ],
        "components/Buttons/SidebarActionButton/index.ts": [
            'import React from "react";',
            "...",
        ],
        "pages/api/chat.ts": [
            'import { NextApiRequest, NextApiResponse } from "next";',
            "...",
        ],
    }

  def test_all_files_returned(self):
    result = format_files_into_prompt_format(self.files)
    for file_name in self.files:
      self.assertIn(file_name, result)

  def test_specific_files_returned(self):
    unique_files = {"pages/api/chat.ts"}
    result = format_files_into_prompt_format(self.files, unique_files)
    self.assertIn("pages/api/chat.ts", result)
    self.assertNotIn("components/Sidebar/index.ts", result)
    self.assertNotIn("components/Buttons/SidebarActionButton/index.ts", result)


extension_to_language = {
    ".feature": "Cucumber",
    ".abap": "abap",
    ".adb": "ada",
    ".ads": "ada",
    ".ada": "ada",
    ".ahk": "ahk",
    ".ahkl": "ahk",
    ".as": "as",
    ".as3": "as3",
    ".asy": "asy",
    ".sh": "bash",
    ".ksh": "bash",
    ".bash": "bash",
    ".ebuild": "bash",
    ".eclass": "bash",
    ".bat": "bat",
    ".cmd": "bat",
    ".befunge": "befunge",
    ".bmx": "blitzmax",
    ".boo": "boo",
    ".bf": "brainfuck",
    ".b": "brainfuck",
    ".c": "c",
    ".h": "c",
    ".cfm": "cfm",
    ".cfml": "cfm",
    ".cfc": "cfm",
    ".tmpl": "cheetah",
    ".spt": "cheetah",
    ".cl": "cl",
    ".lisp": "cl",
    ".el": "cl",
    ".clj": "clojure",
    ".cljs": "clojure",
    ".cmake": "cmake",
    "CMakeLists.txt": "cmake",
    ".coffee": "coffeescript",
    ".sh-session": "console",
    "control": "control",
    ".cpp": "cpp",
    ".hpp": "cpp",
    ".c++": "cpp",
    ".h++": "cpp",
    ".cc": "cpp",
    ".hh": "cpp",
    ".cxx": "cpp",
    ".hxx": "cpp",
    ".pde": "cpp",
    ".cs": "csharp",
    ".css": "css",
    ".pyx": "cython",
    ".pxd": "cython",
    ".pxi": "cython",
    ".d": "d",
    ".di": "d",
    ".pas": "delphi",
    ".diff": "diff",
    ".patch": "diff",
    ".dpatch": "dpatch",
    ".darcspatch": "dpatch",
    ".duel": "duel",
    ".jbst": "duel",
    ".dylan": "dylan",
    ".dyl": "dylan",
    ".erb": "erb",
    ".erl-sh": "erl",
    ".erl": "erlang",
    ".hrl": "erlang",
    ".evoque": "evoque",
    ".factor": "factor",
    ".flx": "felix",
    ".flxh": "felix",
    ".f": "fortran",
    ".f90": "fortran",
    ".s": "gas",
    ".kid": "genshi",
    ".vert": "glsl",
    ".frag": "glsl",
    ".geo": "glsl",
    ".plot": "gnuplot",
    ".plt": "gnuplot",
    ".go": "go",
    ".haml": "haml",
    ".hs": "haskell",
    ".html": "html",
    ".htm": "html",
    ".xhtml": "html",
    ".xslt": "html",
    ".hx": "hx",
    ".hy": "hybris",
    ".hyb": "hybris",
    ".ini": "ini",
    ".cfg": "ini",
    ".io": "io",
    ".ik": "ioke",
    ".weechatlog": "irc",
    ".jade": "jade",
    ".java": "java",
    ".js": "js",
    ".jsp": "jsp",
    ".lhs": "lhs",
    ".ll": "llvm",
    ".lgt": "logtalk",
    ".lua": "lua",
    ".wlua": "lua",
    ".mak": "make",
    "Makefile": "make",
    "makefile": "make",
    ".mao": "mako",
    ".maql": "maql",
    ".mhtml": "mason",
    ".mc": "mason",
    ".mi": "mason",
    "autohandler": "mason",
    "dhandler": "mason",
    ".md": "markdown",
    ".mo": "modelica",
    ".def": "modula2",
    ".mod": "modula2",
    ".moo": "moocode",
    ".mu": "mupad",
    ".mxml": "mxml",
    ".myt": "myghty",
    "autodelegate": "myghty",
    ".asm": "nasm",
    ".ASM": "nasm",
    ".ns2": "newspeak",
    ".objdump": "objdump",
    ".m": "objectivec",
    ".j": "objectivej",
    ".ml": "ocaml",
    ".mli": "ocaml",
    ".mll": "ocaml",
    ".mly": "ocaml",
    ".ooc": "ooc",
    ".pl": "perl",
    ".pm": "perl",
    ".php": "php",
    ".ps": "postscript",
    ".eps": "postscript",
    ".pot": "pot",
    ".po": "pot",
    ".pov": "pov",
    ".inc": "pov",
    ".prolog": "prolog",
    ".pro": "prolog",
    ".properties": "properties",
    ".proto": "protobuf",
    ".py3tb": "py3tb",
    ".pytb": "pytb",
    ".py": "python",
    ".pyw": "python",
    ".sc": "python",
    "SConstruct": "python",
    "SConscript": "python",
    ".tac": "python",
    ".R": "r",
    ".rb": "rb",
    ".rbw": "rb",
    "Rakefile": "rb",
    ".rake": "rb",
    ".gemspec": "rb",
    ".rbx": "rb",
    ".duby": "rb",
    ".Rout": "rconsole",
    ".r": "rebol",
    ".r3": "rebol",
    ".cw": "redcode",
    ".rhtml": "rhtml",
    ".rst": "rst",
    ".rest": "rst",
    ".sass": "sass",
    ".scala": "scala",
    ".scaml": "scaml",
    ".scm": "scheme",
    ".scss": "scss",
    ".st": "smalltalk",
    ".tpl": "smarty",
    "sources.list": "sourceslist",
    ".S": "splus",
    ".sql": "sql",
    ".sqlite3-console": "sqlite3",
    "squid.conf": "squidconf",
    ".ssp": "ssp",
    ".tcl": "tcl",
    ".tcsh": "tcsh",
    ".csh": "tcsh",
    ".tex": "tex",
    ".aux": "tex",
    ".toc": "tex",
    ".txt": "text",
    ".v": "v",
    ".sv": "v",
    ".vala": "vala",
    ".vapi": "vala",
    ".vb": "vbnet",
    ".bas": "vbnet",
    ".vm": "velocity",
    ".fhtml": "velocity",
    ".vim": "vim",
    ".vimrc": "vim",
    ".xml": "xml",
    ".xsl": "xml",
    ".rss": "xml",
    ".xsd": "xml",
    ".wsdl": "xml",
    ".xqy": "xquery",
    ".xquery": "xquery",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".ts": "typescript",
    ".tsx": "typescript",
}
