import pytest
from task_7 import filter_by_substring

def test_filter_by_substring():
	assert filter_by_substring([], 'a') == []
	assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
	assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b') == ['abc', 'bacd']
	assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'e') == ['cde']
	assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z') == []
