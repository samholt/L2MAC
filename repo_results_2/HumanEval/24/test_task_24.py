import pytest
from task_24 import largest_divisor

def test_largest_divisor():
	assert largest_divisor(15) == 5
	assert largest_divisor(16) == 8
	assert largest_divisor(17) == 1
	assert largest_divisor(18) == 9
	assert largest_divisor(19) == 1
	assert largest_divisor(1) == None
	assert largest_divisor(7) == 1

