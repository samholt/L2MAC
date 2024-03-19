import pytest
from task_151 import double_the_difference

def test_double_the_difference():
	assert double_the_difference([1, 3, 2, 0]) == 10
	assert double_the_difference([-1, -2, 0]) == 0
	assert double_the_difference([9, -2]) == 81
	assert double_the_difference([0]) == 0
	assert double_the_difference([]) == 0
