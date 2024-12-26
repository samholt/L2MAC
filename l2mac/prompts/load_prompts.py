"""
This module provides functionality to load L2MAC prompts from YAML files.

Classes:
  L2MACPrompts: A Pydantic model representing the structure of L2MAC prompts.

Functions:
  get_l2mac_prompts(prompts_file_path: Optional[str], domain: Domain) ->
    L2MACPrompts:
      Loads the L2MAC prompts from a given file path or a default file based
      on the domain.

Exceptions:
  FileNotFoundError: Raised when the specified prompts file path does not exist.
  ValidationError: Raised when the prompts file content does not match the
    expected structure.
"""
import os
from importlib import resources
from typing import Optional

import yaml
from pydantic import BaseModel, ValidationError

from l2mac.utils.run import Domain


class L2MACPrompts(BaseModel):
  system: str
  first_message: str
  reflect_on_prompt_program: str
  test_writing_advice: str
  control_unit_execute_instruction: str
  control_unit_exhaust_context_window: str
  control_unit_instruction_complete_summarize_output: str
  control_unit_instruction_erroring_fix_the_code: str
  control_unit_cycle_message_to_check_if_instruction_complete: str


def get_l2mac_prompts(prompts_file_path: Optional[str],
                      domain: Domain) -> L2MACPrompts:
  """
    Loads the L2MAC prompts from a given file path.

    Args:
    prompts_file_path Optional(str): The path to the L2MAC prompts file.

    Returns:
    list: The loaded L2MAC prompts as L2MAC prompt objects
    """
  if prompts_file_path is not None:
    if os.path.isfile(prompts_file_path):
      with open(prompts_file_path, "r", encoding="utf-8") as file:
        prompts_data = yaml.safe_load(file)
        try:
          return L2MACPrompts(**prompts_data)
        except ValidationError as e:
          print(f"Invalid prompts file at `{prompts_file_path}`:", e)
          raise e
    else:
      raise FileNotFoundError(
          f"File not found at `prompts_file_path` of {prompts_file_path}")
  elif domain == Domain.CODEBASE:
    prompts_file = "codebase.yaml"
  elif domain == Domain.BOOK:
    prompts_file = "book.yaml"
  elif domain == Domain.CUSTOM:
    prompts_file = "custom.yaml"
  else:
    raise ValueError(f"Unsupported domain: {domain}")

  prompts_path = resources.files("l2mac.prompts").joinpath(prompts_file)
  with prompts_path.open("r", encoding="utf-8") as file:
    prompts_data = yaml.safe_load(file)
    try:
      return L2MACPrompts(**prompts_data)
    except ValidationError as e:
      print(f"Invalid prompts file at `{prompts_file}`:", e)
      raise e
