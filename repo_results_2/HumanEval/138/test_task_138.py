import pytest
from task_138 import is_equal_to_sum_even

def test_is_equal_to_sum_even():
	assert is_equal_to_sum_even(4) == False
	assert is_equal_to_sum_even(6) == False
	assert is_equal_to_sum_even(8) == True
	assert is_equal_to_sum_even(10) == True
	assert is_equal_to_sum_even(11) == False
	assert is_equal_to_sum_even(12) == True
