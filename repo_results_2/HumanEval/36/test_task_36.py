import pytest
from task_36 import fizz_buzz

def test_fizz_buzz():
	assert fizz_buzz(50) == 0
	assert fizz_buzz(78) == 2
	assert fizz_buzz(79) == 3
	assert fizz_buzz(100) == 3
	assert fizz_buzz(200) == 6
