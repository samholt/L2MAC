import pytest
from task_55 import fib

def test_fib():
	assert fib(0) == 0
	assert fib(1) == 1
	assert fib(2) == 1
	assert fib(3) == 2
	assert fib(10) == 55
	assert fib(20) == 6765
