import pytest
from task_142 import sum_squares

def test_sum_squares():
	assert sum_squares([1,2,3]) == 6
	assert sum_squares([]) == 0
	assert sum_squares([-1,-5,2,-1,-5]) == -126
	assert sum_squares([1,2,3,4,5,6,7,8,9,10]) == 1039
	assert sum_squares([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]) == -707
