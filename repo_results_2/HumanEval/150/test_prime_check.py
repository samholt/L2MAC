import pytest
from prime_check import is_prime

def test_is_prime():
	"""Test the is_prime function."""
	assert is_prime(2) == True
	assert is_prime(3) == True
	assert is_prime(5) == True
	assert is_prime(7) == True
	assert is_prime(11) == True
	assert is_prime(1) == False
	assert is_prime(4) == False
	assert is_prime(6) == False
	assert is_prime(8) == False
	assert is_prime(9) == False
