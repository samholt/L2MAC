import pytest
from task_25 import factorize

def test_factorize():
	assert factorize(8) == [2, 2, 2]
	assert factorize(25) == [5, 5]
	assert factorize(70) == [2, 5, 7]
