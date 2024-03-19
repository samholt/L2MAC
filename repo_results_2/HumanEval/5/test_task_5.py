import pytest
from task_5 import intersperse

def test_intersperse():
	assert intersperse([], 4) == []
	assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
	assert intersperse([-1, -2, -3], 0) == [-1, 0, -2, 0, -3]
	assert intersperse([1, 1, 1], -1) == [1, -1, 1, -1, 1]
	assert intersperse([5], 2) == [5]
	assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
