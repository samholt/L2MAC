import pytest
from task_8 import sum_product

def test_sum_product_empty():
	assert sum_product([]) == (0, 1)

def test_sum_product_numbers():
	assert sum_product([1, 2, 3, 4]) == (10, 24)
