"""
This module provides utility functions and classes for handling various tasks 
such as seeding random number generators, converting Pydantic models to 
dot-accessible dictionaries, and loading prompt programs from files or strings.

Classes:
  Domain (Enum): Enumeration of different domains.
  DebuggingLevel (Enum): Enumeration of different debugging levels.
  DotDict (dict): A dictionary subclass that supports dot notation access to
    keys.

Functions:
  seed_all(seed=None): Sets the seeds for torch, numpy, and random modules.
  to_dotdict(obj): Converts Pydantic models to DotDict recursively.
  load_prompt_program(input_string: str): Loads a prompt program from a given
    file path or parses it from a string in list format.
"""
import ast
import os
import random
from enum import Enum
from time import time

import numpy as np
from pydantic import BaseModel


class Domain(str, Enum):
  CODEBASE = "codebase"
  BOOK = "book"
  CUSTOM = "custom"  # Contributors add your custom domains here


class DebuggingLevel(str, Enum):
  DEBUG = "debug"
  INFO = "info"
  WARN = "warn"
  ERROR = "error"


def seed_all(seed=None):
  """
    Set the torch, numpy, and random module seeds based on the seed
    specified in config. If there is no seed or it is None, a time-based
    seed is used instead and is written to config.
    """
  # Default uses current time in milliseconds, modulo 1e9
  if seed is None:
    seed = round(time() * 1000) % int(1e9)

  # Set the seeds using the shifted seed
  np.random.seed(seed)
  random.seed(seed)


class DotDict(dict):
  """Dictionary subclass that supports dot notation access to keys."""
  def __getattr__(self, name):
    return self.get(name, None)

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    del self[name]


def to_dotdict(obj):
  """Function to convert Pydantic models to DotDict recursively."""
  if isinstance(obj, dict):
    return DotDict({k: to_dotdict(v) for k, v in obj.items()})
  elif isinstance(obj, BaseModel):
    return DotDict({k: to_dotdict(v) for k, v in obj.dict().items()})
  elif isinstance(obj, list):
    return [to_dotdict(item) for item in obj]
  else:
    return obj


def load_prompt_program(input_string: str):
  """
    Loads a prompt program from a given file path or parses it from a string in
    list format.

    Args:
    input_string (str): The path to the prompt program file or the prompt
      program as a string in a list format.

    Returns:
    list: The loaded or parsed prompt program as a list, or None if not found
      or invalid.
    """
  # check input_string is a list type
  if isinstance(input_string, list) and len(input_string) >= 1:
    return input_string
  # Check if the input string is a path to a file
  if os.path.isfile(input_string):
    try:
      with open(input_string, "r", encoding="utf-8") as file:
        # Read the file content and attempt to parse it
        file_content = file.read()
        return ast.literal_eval(file_content)
    except (SyntaxError, ValueError, IOError) as e:
      print(
          "Error reading or parsing `prompt_program` file path of"
          f"{input_string} | Error: {e}"
      )
      raise e
  else:
    # Try to parse it directly as a list from the string
    try:
      result = ast.literal_eval(input_string)
      if isinstance(result, list):
        return result
      else:
        raise ValueError("Input of `prompt_program` is not a list.")
    except (SyntaxError, ValueError) as e:
      print(
          "Error reading or parsing `prompt_program` string encoded of "
          f"{input_string} | Error: {e}"
      )
      raise e
