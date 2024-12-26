"""
Unit tests for the l2mac utility functions.

This module contains tests for the following functions:
- CustomTokenLimitError: Custom exception for token limit errors.
- hash_messages: Hashes a list of messages into a single string.
- detect_cycles: Detects cycles in a list of dictionaries.
- clean_string: Cleans a file path string to extract the file name.

Each test function verifies the expected behavior of these utility functions.
"""
from l2mac.utils.l2mac import (
    CustomTokenLimitError,
    clean_string,
    detect_cycles,
    hash_messages,
)


def test_l2mac_internal_errors():
  try:
    raise CustomTokenLimitError
  except CustomTokenLimitError:
    assert True


def test_l2mac():
  assert True


def test_hash_messages_empty_list():
  result = hash_messages([])
  assert isinstance(result, str)
  assert len(result) == 64


def test_hash_messages_non_empty_list():
  input_list = ["message1", "message2"]
  result = hash_messages(input_list)
  assert isinstance(result, str)
  assert len(result) == 64


def test_detect_cycles_no_cycle():
  lst = [{"a": 1}, {"b": 2}, {"c": 3}]
  result = detect_cycles(lst)
  assert result is False


def test_detect_cycles_with_cycle():
  lst = [{"a": 1}, {"b": 2}, {"a": 1}, {"b": 2}]
  result = detect_cycles(lst, cycle_lengths=[2])
  assert result is True


def test_clean_string():
  input_string = "/tmp/somepath/file.txt"
  result = clean_string(input_string)
  assert result == "/file.txt"


if __name__ == "__main__":
  test_l2mac()
  test_l2mac_internal_errors()
  test_hash_messages_empty_list()
  test_hash_messages_non_empty_list()
  test_detect_cycles_no_cycle()
  test_detect_cycles_with_cycle()
  test_clean_string()
  print("l2mac test passed")
