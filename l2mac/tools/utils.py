"""
This module provides utilities for file and directory operations,
as well as some basic numerical operations using numpy.

Modules:
    os: Provides a way of using operating system dependent functionality.
    re: Provides regular expression matching operations.
    shutil: Provides high-level file operations.
    numpy: Provides support for large, multi-dimensional arrays and matrices.

Functions:
    (List any functions you have in this module here)
"""
import os
import re
import shutil

import numpy as np


def write_files_from_dict(file_dict, base_dir="output"):
  """
    Writes files to a folder based on the given dictionary.

    :param file_dict: Dictionary with filenames as keys and lists of file
                        content as values.
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
    with open(full_path, "w", encoding="utf-8") as f:
      for line in lines:
        f.write(line + "\n")


def fix_line_spacings(strings):
  # Regular expression pattern to match 'number: ' at the beginning of
  #   each string
  lines = []
  for line in strings:
    leading_spaces = len(line) - len(line.lstrip(" "))
    leading_spaces = int(np.ceil(leading_spaces / 2) * 2)
    line = " " * leading_spaces + line.lstrip(" ")
    lines.append(line)
  return lines


def remove_line_numbers(strings):
  # Regular expression pattern to match 'number: ' at the beginning of
  #   each string
  pattern = r"^\d+:\s"
  return [re.sub(pattern, "", s) for s in strings]
