import pytest
from task_80 import is_happy

def test_is_happy():
	assert is_happy('a') == False
	assert is_happy('aa') == False
	assert is_happy('abcd') == True
	assert is_happy('aabb') == False
	assert is_happy('adb') == True
	assert is_happy('xyy') == False
