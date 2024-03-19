from prime_utils import is_prime

def is_multiply_prime(a):
	"""Check if a number is the product of three prime numbers."""
	for i in range(2, a):
		if a % i != 0 or not is_prime(i):
			continue
		for j in range(i, a // i + 1):
			if a % (i * j) != 0 or not is_prime(j):
				continue
			for k in range(j, a // (i * j) + 1):
				if i * j * k == a and is_prime(k):
					return True
	return False
