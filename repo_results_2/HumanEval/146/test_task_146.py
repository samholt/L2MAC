import pytest
from task_146 import specialFilter

def test_specialFilter():
	assert specialFilter([15, -73, 14, -15]) == 1
	assert specialFilter([33, -2, -3, 45, 21, 109]) == 2
	assert specialFilter([11, 13, 15, 17, 19]) == 5
	assert specialFilter([-11, -13, -15, -17, -19]) == 0
	assert specialFilter([10, 20, 30, 40, 50]) == 0
