import pytest
from task_62 import derivative

def test_derivative():
	assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
	assert derivative([1, 2, 3]) == [2, 6]
	assert derivative([]) == []
	assert derivative([5]) == []
	assert derivative([1, 0, 3, 0, 5]) == [0, 6, 0, 20]
