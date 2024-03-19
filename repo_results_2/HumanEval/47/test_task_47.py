import pytest
from task_47 import median

def test_median_odd_numbers():
	assert median([1, 2, 3, 4, 5]) == 3

def test_median_even_numbers():
	assert median([1, 2, 3, 4]) == 2.5

def test_median_negative_numbers():
	assert median([-5, -1, -3, -2, -4]) == -3

def test_median_single_element():
	assert median([10]) == 10

def test_median_large_numbers():
	assert median([1000, 2000, 3000, 4000, 5000]) == 3000
