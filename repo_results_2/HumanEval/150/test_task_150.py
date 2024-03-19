import pytest
from task_150 import x_or_y

def test_x_or_y():
	assert x_or_y(7, 34, 12) == 34
	assert x_or_y(15, 8, 5) == 5
	assert x_or_y(2, 10, 20) == 10
	assert x_or_y(4, 10, 20) == 20
	assert x_or_y(11, 100, 200) == 100
	assert x_or_y(9, 100, 200) == 200
