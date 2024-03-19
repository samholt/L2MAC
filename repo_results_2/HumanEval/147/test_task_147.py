import pytest
from task_147 import get_max_triples

def test_get_max_triples():
	assert get_max_triples(5) == 1
	assert get_max_triples(1) == 0
	assert get_max_triples(10) == 36
	assert get_max_triples(7) == 10
	assert get_max_triples(100) == 53361
