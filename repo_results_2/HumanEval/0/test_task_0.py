import pytest
from task_0 import has_close_elements


def test_has_close_elements():
	assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
	assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
	assert has_close_elements([], 0.5) == False
	assert has_close_elements([1.0], 0.5) == False
	assert has_close_elements([1.0, 1.0, 1.0], 0.0) == True
	assert has_close_elements([1.0, 1.5], 0.5) == True
	assert has_close_elements([1.0, 1.5], 0.49) == False
