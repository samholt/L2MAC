import pytest
from task_137 import compare_one

def test_compare_one():
	assert compare_one(1, 2.5) == 2.5
	assert compare_one(1, '2,3') == '2,3'
	assert compare_one('5,1', '6') == '6'
	assert compare_one('1', 1) == None
	assert compare_one(3, 3) == None
	assert compare_one('3.5', '3.5') == None
	assert compare_one(3.5, '3,5') == None
	assert compare_one('3,5', 3.5) == None
	assert compare_one('3,5', '3.5') == None
	assert compare_one('3.5', '3,5') == None

