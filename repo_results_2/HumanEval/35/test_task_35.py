import pytest
from task_35 import max_element

def test_max_element():
	assert max_element([1, 2, 3]) == 3
	assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
	assert max_element([-5, -3, -2]) == -2
	assert max_element([5, 5, 5, 5]) == 5
	assert max_element([1]) == 1
