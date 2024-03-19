import pytest
from task_97 import multiply

def test_multiply_positive_numbers():
	assert multiply(148, 412) == 16
	assert multiply(19, 28) == 72
	assert multiply(2020, 1851) == 0


def test_multiply_negative_numbers():
	assert multiply(14,-15) == 20
	assert multiply(-14,15) == 20
	assert multiply(-14,-15) == 20


def test_multiply_zero():
	assert multiply(0, 1851) == 0
	assert multiply(2020, 0) == 0
	assert multiply(0, 0) == 0

