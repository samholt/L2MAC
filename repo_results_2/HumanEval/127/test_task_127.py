import pytest
from task_127 import intersection

def test_intersection():
	assert intersection((1, 2), (2, 3)) == 'NO'
	assert intersection((-1, 1), (0, 4)) == 'NO'
	assert intersection((-3, -1), (-5, 5)) == 'YES'
	assert intersection((1, 5), (2, 6)) == 'YES'
	assert intersection((1, 7), (2, 8)) == 'YES'
