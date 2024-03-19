import pytest
from task_23 import strlen

def test_strlen():
	assert strlen('') == 0
	assert strlen('abc') == 3
	assert strlen('hello world') == 11
