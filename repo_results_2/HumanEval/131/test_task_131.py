import pytest
from task_131 import digits

def test_digits():
	assert digits(1) == 1
	assert digits(4) == 0
	assert digits(235) == 15
	assert digits(1234567890) == 945
	assert digits(2468) == 0
