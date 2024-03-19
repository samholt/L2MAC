import pytest
from task_28 import concatenate

def test_concatenate_empty_list():
	assert concatenate([]) == ''

def test_concatenate_abc():
	assert concatenate(['a', 'b', 'c']) == 'abc'

