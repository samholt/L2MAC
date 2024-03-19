import pytest
from task_133 import sum_squares

def test_sum_squares():
	assert sum_squares([1,2,3]) == 14
	assert sum_squares([1,4,9]) == 98
	assert sum_squares([1,3,5,7]) == 84
	assert sum_squares([1.4,4.2,0]) == 29
	assert sum_squares([-2.4,1,1]) == 6
