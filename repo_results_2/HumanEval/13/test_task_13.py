import pytest
from task_13 import greatest_common_divisor

def test_greatest_common_divisor():
	assert greatest_common_divisor(3, 5) == 1
	assert greatest_common_divisor(25, 15) == 5
	assert greatest_common_divisor(17, 13) == 1
	assert greatest_common_divisor(100, 10) == 10
	assert greatest_common_divisor(36, 24) == 12
