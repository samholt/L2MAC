import pytest
from task_14 import all_prefixes

def test_all_prefixes():
	assert all_prefixes('abc') == ['a', 'ab', 'abc']
	assert all_prefixes('') == []
	assert all_prefixes('a') == ['a']
	assert all_prefixes('ab') == ['a', 'ab']

