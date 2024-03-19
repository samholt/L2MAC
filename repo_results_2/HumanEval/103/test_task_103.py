import pytest
from task_103 import rounded_avg

def test_rounded_avg():
	assert rounded_avg(1, 5) == '0b11'
	assert rounded_avg(7, 5) == -1
	assert rounded_avg(10, 20) == '0b1111'
	assert rounded_avg(20, 33) == '0b11010'
	assert rounded_avg(3, 3) == '0b11'
	assert rounded_avg(100, 200) == '0b10010110'
	assert rounded_avg(0, 0) == '0b0'
