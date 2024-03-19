import pytest
from task_68 import pluck

def test_pluck():
	assert pluck([4,2,3]) == [2, 1]
	assert pluck([1,2,3]) == [2, 1]
	assert pluck([]) == []
	assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
	assert pluck([1,3,5,7]) == []
	assert pluck([2,2,2,2]) == [2, 0]
	assert pluck([1,1,1,2]) == [2, 3]
