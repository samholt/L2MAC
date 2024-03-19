import pytest
from task_43 import pairs_sum_to_zero

def test_pairs_sum_to_zero():
	assert pairs_sum_to_zero([1, 3, 5, 0]) == False
	assert pairs_sum_to_zero([1, 3, -2, 1]) == False
	assert pairs_sum_to_zero([1, 2, 3, 7]) == False
	assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) == True
	assert pairs_sum_to_zero([1]) == False
	assert pairs_sum_to_zero([]) == False
