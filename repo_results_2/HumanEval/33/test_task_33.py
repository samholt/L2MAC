import pytest
from task_33 import sort_third

def test_sort_third():
	# Test case from the problem statement
	assert sort_third([1, 2, 3]) == [1, 2, 3]
	assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

	# Additional test cases
	# Test an empty list
	assert sort_third([]) == []

	# Test a list with one element
	assert sort_third([1]) == [1]

	# Test a list where all elements are the same
	assert sort_third([1, 1, 1, 1]) == [1, 1, 1, 1]

	# Test a list where the elements at indices divisible by three are already sorted
	assert sort_third([1, 2, 3, 4]) == [1, 2, 3, 4]

	# Test a list where the elements at indices divisible by three are in reverse order
	assert sort_third([4, 2, 3, 1]) == [1, 2, 3, 4]

