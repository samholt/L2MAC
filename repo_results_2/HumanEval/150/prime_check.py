import math

def is_prime(n):
	"""Check if a number is prime.

	A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
	This function checks if a number n is prime by iterating from 2 to the square root of n and checking if n is divisible by any of these numbers.
	If it is, then n is not prime. Otherwise, n is prime.

	Args:
		n (int): The number to check.

	Returns:
		bool: True if n is prime, False otherwise.
	"""
	if n <= 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, math.isqrt(n) + 1, 2):
		if n % i == 0:
			return False
	return True
