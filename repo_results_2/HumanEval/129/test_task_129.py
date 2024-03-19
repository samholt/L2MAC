import pytest
from task_129 import minPath

def test_minPath_example1():
	assert minPath([[1,2,3], [4,5,6], [7,8,9]], 3) == [1, 2, 1]

def test_minPath_example2():
	assert minPath([[5,9,3], [4,1,6], [7,8,2]], 1) == [1]

def test_minPath_2x2_grid():
	assert minPath([[1,2], [3,4]], 2) == [1, 2]

def test_minPath_4x4_grid():
	assert minPath([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 4) == [1, 2, 1, 2]

def test_minPath_duplicate_values():
	assert minPath([[1,2,3], [4,1,6], [7,8,9]], 3) == [1, 2, 1]

def test_minPath_negative_values():
	assert minPath([[-1,-2,-3], [-4,-5,-6], [-7,-8,-9]], 2) == [-9, -8]
