import pytest
from task_46 import fib4

def test_fib4():
	assert fib4(0) == 0
	assert fib4(1) == 0
	assert fib4(2) == 2
	assert fib4(3) == 0
	assert fib4(5) == 4
	assert fib4(6) == 8
	assert fib4(7) == 14
	assert fib4(10) == 104
	assert fib4(20) == 73552

