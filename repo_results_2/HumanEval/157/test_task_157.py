import pytest
from task_157 import right_angle_triangle

def test_right_angle_triangle():
	assert right_angle_triangle(3, 4, 5) == True
	assert right_angle_triangle(1, 2, 3) == False
	assert right_angle_triangle(5, 12, 13) == True
	assert right_angle_triangle(2, 2, 2) == False
