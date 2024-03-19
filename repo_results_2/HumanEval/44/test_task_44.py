import pytest
from task_44 import change_base, change_base_v2


def test_change_base():
	assert change_base(8, 3) == '22'
	assert change_base(8, 2) == '1000'
	assert change_base(7, 2) == '111'
	assert change_base(0, 2) == ''
	assert change_base(1, 2) == '1'


def test_change_base_v2():
	assert change_base_v2(255, 16) == 'ff'
	assert change_base_v2(0, 16) == ''
	assert change_base_v2(1, 16) == '1'
	assert change_base_v2(10, 16) == 'a'
	assert change_base_v2(15, 16) == 'f'
