import pytest
from task_6 import parse_nested_parens


def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('((()))') == [3]
    assert parse_nested_parens('(()()())') == [2]
    assert parse_nested_parens('') == []
