import pytest
from task_60 import sum_to_n

def test_sum_to_n():
	assert sum_to_n(30) == 465
	assert sum_to_n(100) == 5050
	assert sum_to_n(5) == 15
	assert sum_to_n(10) == 55
	assert sum_to_n(1) == 1
