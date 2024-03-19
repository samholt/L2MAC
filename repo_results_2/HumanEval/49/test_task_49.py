import pytest
from task_49 import modp

def test_modp():
	assert modp(3, 5) == 3
	assert modp(1101, 101) == 2
	assert modp(0, 101) == 1
	assert modp(3, 11) == 8
	assert modp(100, 101) == 1
