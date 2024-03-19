def is_prime(n):
	"""Check if a number is prime."""
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True
