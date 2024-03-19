import pytest
from task_57 import monotonic

def test_monotonic():
	assert monotonic([1, 2, 4, 20]) == True
	assert monotonic([1, 20, 4, 10]) == False
	assert monotonic([4, 1, 0, -10]) == True
	assert monotonic([10, 10, 10, 10]) == True
	assert monotonic([]) == True
