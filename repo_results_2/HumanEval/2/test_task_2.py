import pytest
from task_2 import truncate_number

def test_truncate_number():
	assert truncate_number(3.5) == 0.5
	assert truncate_number(10.0) == 0.0
	assert truncate_number(0.123456) == 0.123456
	assert truncate_number(123456.789) == 0.789
	assert truncate_number(0.0) == 0.0

