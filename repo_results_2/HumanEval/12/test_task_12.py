import pytest
from task_12 import longest

def test_longest():
	assert longest(['a', 'b', 'c']) == 'a'
	assert longest(['a', 'bb', 'ccc']) == 'ccc'
	assert longest([]) == None
	assert longest(['aaaa', 'bbb', 'cc', 'd']) == 'aaaa'
	assert longest(['a', 'bb', 'c', 'dddd']) == 'dddd'
