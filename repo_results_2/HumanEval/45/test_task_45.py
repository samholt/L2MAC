import pytest
from task_45 import triangle_area

def test_triangle_area():
	assert triangle_area(5, 3) == 7.5
	assert triangle_area(10, 2) == 10.0
	assert triangle_area(0, 0) == 0.0
	assert triangle_area(1, 1) == 0.5
	assert triangle_area(-5, 3) == -7.5
