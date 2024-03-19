import pytest
from task_92 import any_int

def test_any_int():
	assert any_int(5, 2, 7) == True
	assert any_int(3, 2, 2) == False
	assert any_int(3, -2, 1) == True
	assert any_int(3.6, -2.2, 2) == False
	assert any_int(3, 2, 'a') == False
