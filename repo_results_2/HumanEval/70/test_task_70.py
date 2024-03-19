import pytest
from task_70 import strange_sort_list

def test_strange_sort_list():
	assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
	assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
	assert strange_sort_list([]) == []
	assert strange_sort_list([1]) == [1]
	assert strange_sort_list([2, 1]) == [1, 2]
	assert strange_sort_list([3, 2, 1]) == [1, 3, 2]
