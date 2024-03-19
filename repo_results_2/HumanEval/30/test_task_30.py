import pytest
from task_30 import get_positive

def test_get_positive():
	assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
	assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
	assert get_positive([]) == []
	assert get_positive([-1, -2, -3]) == []
	assert get_positive([1, 2, 3]) == [1, 2, 3]
