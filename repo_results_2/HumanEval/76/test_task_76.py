import pytest
from task_76 import is_simple_power

def test_is_simple_power():
	assert is_simple_power(1, 4) == True
	assert is_simple_power(2, 2) == True
	assert is_simple_power(8, 2) == True
	assert is_simple_power(3, 2) == False
	assert is_simple_power(3, 1) == False
	assert is_simple_power(5, 3) == False
