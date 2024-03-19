import pytest
from task_106 import f

def test_f():
	assert f(5) == [1, 2, 6, 24, 15]
	assert f(3) == [1, 2, 6]
	assert f(1) == [1]
	assert f(0) == []
