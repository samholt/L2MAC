def largest_prime_factor(n: int):
	"""Return the largest prime factor of n. Assume n > 1 and is not a prime.
	>>> largest_prime_factor(13195)
	29
	>>> largest_prime_factor(2048)
	2
	"""
	if n <= 1:
		return None
	factor = 2
	while n > 1:
		if n % factor == 0:
			n /= factor
		else:
			factor += 1
	return factor

def test_largest_prime_factor():
	assert largest_prime_factor(13195) == 29
	assert largest_prime_factor(2048) == 2
	assert largest_prime_factor(100) == 5
	assert largest_prime_factor(81) == 3
	assert largest_prime_factor(49) == 7
