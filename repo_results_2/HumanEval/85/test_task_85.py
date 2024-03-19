import pytest
from task_85 import add

def test_add():
	assert add([4, 2, 6, 7]) == 2
	assert add([1, 2, 3, 4, 5, 6]) == 12
	assert add([1, 3, 5, 7, 9]) == 0
	assert add([2, 4, 6, 8]) == 12
