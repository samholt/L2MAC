import pytest
from task_66 import digitSum

def test_empty_string():
	"""Test case for an empty string"""
	assert digitSum('') == 0

def test_no_uppercase():
	"""Test case for a string with no uppercase characters"""
	assert digitSum('abc') == 0

def test_single_uppercase():
	"""Test case for a string with a single uppercase character"""
	assert digitSum('abcD') == 68

def test_multiple_uppercase():
	"""Test case for a string with multiple uppercase characters"""
	assert digitSum('abcDE') == 137

def test_mixed_case():
	"""Test case for a string with both uppercase and lowercase characters"""
	assert digitSum('abcDEf') == 137
