import pytest
from task_73 import smallest_change

def test_smallest_change():
	assert smallest_change([1,2,3,5,4,7,9,6]) == 4
	assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
	assert smallest_change([1, 2, 3, 2, 1]) == 0
	assert smallest_change([1, 1, 1, 1, 1]) == 0
	assert smallest_change([1, 2, 3, 4, 5]) == 2
