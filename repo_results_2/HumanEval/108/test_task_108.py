import pytest
from task_108 import count_nums

def test_count_nums():
	assert count_nums([]) == 0
	assert count_nums([-1, 11, -11]) == 1
	assert count_nums([1, 1, 2]) == 3
	assert count_nums([0, 0, 0]) == 0
	assert count_nums([-1, -1, -1]) == 0
	assert count_nums([10, 20, 30]) == 3
	assert count_nums([-10, -20, -30]) == 0
