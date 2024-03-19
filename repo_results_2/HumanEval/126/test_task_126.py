import pytest
from task_126 import is_sorted

def test_is_sorted():
	assert is_sorted([5]) == True
	assert is_sorted([1, 2, 3, 4, 5]) == True
	assert is_sorted([1, 3, 2, 4, 5]) == False
	assert is_sorted([1, 2, 3, 4, 5, 6]) == True
	assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
	assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False
	assert is_sorted([1, 2, 2, 3, 3, 4]) == False
	assert is_sorted([1, 2, 2, 2, 3, 4]) == False
