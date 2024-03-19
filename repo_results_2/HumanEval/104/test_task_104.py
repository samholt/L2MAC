import pytest
from task_104 import unique_digits

def test_unique_digits():
	assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
	assert unique_digits([152, 323, 1422, 10]) == []
	assert unique_digits([13579, 111, 333, 555, 777, 999]) == [111, 333, 555, 777, 999, 13579]
	assert unique_digits([2, 4, 6, 8]) == []
