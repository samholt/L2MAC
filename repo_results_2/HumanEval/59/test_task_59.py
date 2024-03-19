import pytest
from task_59 import largest_prime_factor

def test_largest_prime_factor():
	assert largest_prime_factor(13195) == 29
	assert largest_prime_factor(2048) == 2
	assert largest_prime_factor(100) == 5
	assert largest_prime_factor(999) == 37
	assert largest_prime_factor(500) == 5
