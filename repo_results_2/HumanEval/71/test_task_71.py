import pytest
from task_71 import triangle_area

def test_triangle_area():
	assert triangle_area(3, 4, 5) == 6.00
	assert triangle_area(1, 2, 10) == -1
	assert triangle_area(0, 0, 0) == -1
	assert triangle_area(3, 4, -5) == -1
	assert triangle_area(5, 12, 13) == 30.00
