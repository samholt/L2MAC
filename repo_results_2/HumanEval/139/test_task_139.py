import pytest
from task_139 import special_factorial

def test_special_factorial():
	assert special_factorial(4) == 288
	assert special_factorial(0) == 1
	assert special_factorial(1) == 1
	assert special_factorial(2) == 2
	assert special_factorial(3) == 12
	assert special_factorial(5) == 34560
	assert special_factorial(6) == 24883200

