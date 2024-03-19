import pytest
from task_163 import generate_integers

def test_generate_integers():
	assert generate_integers(2, 8) == [2, 4, 6, 8]
	assert generate_integers(8, 2) == [2, 4, 6, 8]
	assert generate_integers(10, 15) == [10, 12, 14]
	assert generate_integers(5, 5) == []
	assert generate_integers(6, 6) == [6]
	assert generate_integers(1, 1) == []
