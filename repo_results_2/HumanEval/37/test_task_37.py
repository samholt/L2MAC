import pytest
from task_37 import sort_even

def test_sort_even():
	assert sort_even([]) == []
	assert sort_even([1]) == [1]
	assert sort_even([1, 2, 3]) == [1, 2, 3]
	assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
	assert sort_even([5, 5, 5, 5]) == [5, 5, 5, 5]
	assert sort_even([5, 6, 7, 8, 9]) == [5, 6, 7, 8, 9]
	assert sort_even([9, 8, 7, 6, 5]) == [5, 8, 7, 6, 9]
