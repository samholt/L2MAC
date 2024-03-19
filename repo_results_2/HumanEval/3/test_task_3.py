import pytest
from task_3 import below_zero

def test_below_zero():
	assert below_zero([1, 2, 3]) == False
	assert below_zero([1, 2, -4, 5]) == True
	assert below_zero([10, -2, -8]) == False
	assert below_zero([10, -2, -9]) == True
	assert below_zero([]) == False
