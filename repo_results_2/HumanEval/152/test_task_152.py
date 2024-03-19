import pytest
from task_152 import compare

def test_compare():
	assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]
	assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]
	assert compare([0,0,0,0,0,0],[0,0,0,0,0,0]) == [0,0,0,0,0,0]
	assert compare([1,1,1,1,1,1],[0,0,0,0,0,0]) == [1,1,1,1,1,1]
	assert compare([1,2,3,4,5,6],[-1,-2,-3,-4,-5,-6]) == [2,4,6,8,10,12]
