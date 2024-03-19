import pytest
from task_145 import order_by_points

def test_order_by_points():
	assert order_by_points([1, 11, -1, -11, -12]) == [1, -1, 11, -11, -12]
	assert order_by_points([]) == []
	assert order_by_points([10, 20, 30, 40]) == [10, 20, 30, 40]
	assert order_by_points([40, 30, 20, 10]) == [10, 20, 30, 40]
	assert order_by_points([13, 22, 8, 5, 10]) == [10, 13, 22, 5, 8]
