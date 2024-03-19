import pytest
from task_114 import minSubArraySum

def test_minSubArraySum():
	assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
	assert minSubArraySum([-1, -2, -3]) == -6
	assert minSubArraySum([1, 2, 3, 4, 5]) == 1
	assert minSubArraySum([-1, -2, -3, -4, -5]) == -15
