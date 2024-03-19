import pytest
from task_123 import get_odd_collatz

def test_get_odd_collatz():
	assert get_odd_collatz(5) == [1, 5]
	assert get_odd_collatz(1) == [1]
	assert get_odd_collatz(6) == [1, 3, 5]
	assert get_odd_collatz(11) == [1, 5, 11, 13, 17]
