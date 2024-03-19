import pytest
from task_121 import solution

def test_solution():
	assert solution([]) == 0
	assert solution([1]) == 1
	assert solution([2, 4, 6, 8]) == 0
	assert solution([1, 3, 5, 7]) == 6
	assert solution([2, 1, 4, 3, 6, 5, 8, 7]) == 0
	assert solution([1, 2, 3, 4, 5, 6, 7, 8]) == 16
	assert solution([8, 7, 6, 5, 4, 3, 2, 1]) == 0
