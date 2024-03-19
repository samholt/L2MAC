import pytest
from task_120 import maximum

def test_maximum():
	# Test case 1: Check if the function returns an empty list when the input array is empty
	assert maximum([], 3) == []

	# Test case 2: Check if the function returns an empty list when k is zero
	assert maximum([1, 2, 3], 0) == []

	# Test case 3: Check if the function returns a list of length k with the maximum k numbers in the array
	assert maximum([-3, -4, 5], 3) == [5, -3, -4]
	assert maximum([4, -4, 4], 2) == [4, 4]
	assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
