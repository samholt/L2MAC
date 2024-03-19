import pytest
from task_102 import choose_num

def test_choose_num():
	assert choose_num(12, 15) == 14
	assert choose_num(13, 12) == -1
	assert choose_num(10, 10) == 10
	assert choose_num(11, 11) == -1
	assert choose_num(10, 11) == 10
	assert choose_num(11, 12) == 12
	assert choose_num(1, 100) == 100
	assert choose_num(100, 1) == -1
	assert choose_num(2, 3) == 2
	assert choose_num(3, 2) == -1
