import pytest
from task_29 import filter_by_prefix

def test_filter_by_prefix():
	# Test when strings list is empty
	assert filter_by_prefix([], 'a') == []

	# Test when prefix is empty
	assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']

	# Test when none of the strings start with the prefix
	assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

	# Test when some of the strings start with the prefix
	assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

	# Test when all of the strings start with the prefix
	assert filter_by_prefix(['abc', 'acd', 'ade', 'array'], 'a') == ['abc', 'acd', 'ade', 'array']
