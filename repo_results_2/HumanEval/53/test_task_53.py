import pytest
from task_53 import add

def test_add():
	assert add(2, 3) == 5
	assert add(5, 7) == 12
	assert add(-1, 1) == 0
