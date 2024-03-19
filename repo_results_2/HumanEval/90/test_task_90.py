import pytest
from task_90 import next_smallest


def test_next_smallest():
	assert next_smallest([1, 2, 3, 4, 5]) == 2
	assert next_smallest([5, 1, 4, 3, 2]) == 2
	assert next_smallest([]) == None
	assert next_smallest([1, 1]) == None
	assert next_smallest([1, 2, 2, 3, 3]) == 2
	assert next_smallest([5, 4, 3, 2, 1]) == 2
	assert next_smallest([1]) == None
	assert next_smallest([1, 1, 1, 1, 2]) == 2
