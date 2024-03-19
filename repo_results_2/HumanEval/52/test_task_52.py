import pytest
from task_52 import below_threshold

def test_below_threshold():
	assert below_threshold([], 5) == True
	assert below_threshold([1], 5) == True
	assert below_threshold([1, 2, 3, 4], 5) == True
	assert below_threshold([1, 2, 3, 5], 5) == False
	assert below_threshold([1, 2, 3, 6], 5) == False
