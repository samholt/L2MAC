import pytest
from task_136 import largest_smallest_integers

def test_largest_smallest_integers():
	assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
	assert largest_smallest_integers([]) == (None, None)
	assert largest_smallest_integers([0]) == (None, None)
	assert largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None)
	assert largest_smallest_integers([-2, -4, 1, 3, 5, 7]) == (-2, 1)
	assert largest_smallest_integers([-2, -4, 0, 1, 3, 5, 7]) == (-2, 1)
