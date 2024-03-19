import pytest
from task_78 import hex_key

def test_hex_key():
	assert hex_key('AB') == 1
	assert hex_key('1077E') == 2
	assert hex_key('ABED1A33') == 4
	assert hex_key('123456789ABCDEF0') == 6
	assert hex_key('2020') == 2
	assert hex_key('') == 0
	assert hex_key('0') == 0
	assert hex_key('F') == 0
