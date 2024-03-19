import pytest
from task_130 import tri

def test_tri():
	assert tri(0) == [1]
	assert tri(1) == [1, 3]
	assert tri(2) == [1, 3, 2]
	assert tri(3) == [1, 3, 2, 8]
	assert tri(4) == [1, 3, 2, 8, 3]
	assert tri(5) == [1, 3, 2, 8, 3, 13]
	assert tri(6) == [1, 3, 2, 8, 3, 13, 4]
	assert tri(7) == [1, 3, 2, 8, 3, 13, 4, 24]
