import pytest
from task_116 import sort_array

def test_sort_array():
	assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
	assert sort_array([0, 1, 2, 3, 4]) == [0, 1, 2, 4, 3]
	assert sort_array([]) == []
	assert sort_array([1]) == [1]

	with pytest.raises(TypeError):
		sort_array('not a list')

	with pytest.raises(ValueError):
		sort_array([1, 2, 'not an integer', 4, 5])
		sort_array([1, 2, -3, 4, 5])
