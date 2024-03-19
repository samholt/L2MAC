import pytest
from task_40 import triples_sum_to_zero

def test_triples_sum_to_zero():
	assert triples_sum_to_zero([1, 3, 5, 0]) == False
	assert triples_sum_to_zero([1, 3, -2, 1]) == True
	assert triples_sum_to_zero([1, 2, 3, 7]) == False
	assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
	assert triples_sum_to_zero([1]) == False
	assert triples_sum_to_zero([]) == False
	assert triples_sum_to_zero([-1, 0, 1]) == True
	assert triples_sum_to_zero([-1, -1, 2]) == True
	assert triples_sum_to_zero([-1, -1, 1]) == False
