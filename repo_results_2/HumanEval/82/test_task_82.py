import pytest
from task_82 import is_prime, prime_length

def test_is_prime():
	assert is_prime(2) == True
	assert is_prime(3) == True
	assert is_prime(4) == False
	assert is_prime(5) == True
	assert is_prime(6) == False
	assert is_prime(7) == True
	assert is_prime(8) == False
	assert is_prime(9) == False
	assert is_prime(10) == False

def test_prime_length():
	assert prime_length('Hello') == True
	assert prime_length('abcdcba') == True
	assert prime_length('kittens') == True
	assert prime_length('orange') == False
	assert prime_length('') == False
