import pytest
from task_100 import make_a_pile

def test_make_a_pile_odd():
	assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_even():
	assert make_a_pile(4) == [4, 6, 8, 10]

def test_make_a_pile_one():
	assert make_a_pile(1) == [1]

def test_make_a_pile_zero():
	assert make_a_pile(0) == []
