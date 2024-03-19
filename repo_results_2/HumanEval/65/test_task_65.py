import pytest
from task_65 import circular_shift

def test_circular_shift():
	assert circular_shift(12, 1) == '21'
	assert circular_shift(12, 2) == '12'
	assert circular_shift(123, 1) == '312'
	assert circular_shift(123, 3) == '123'
	assert circular_shift(123, 4) == '321'
	assert circular_shift(5, 1) == '5'
	assert circular_shift(5, 0) == '5'
	assert circular_shift(12, 0) == '12'
	assert circular_shift(12, -1) == '21'
