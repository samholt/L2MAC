def starts_one_ends(n):
	"""
	Given a positive integer n, return the count of the numbers of n-digit
	positive integers that start or end with 1.
	"""
	if not isinstance(n, int) or n <= 0:
		raise ValueError('Input must be a positive integer')
	
	# Calculate the count of n-digit positive integers that start or end with 1
	start_with_1 = 10 ** (n - 1)
	end_with_1 = 10 ** (n - 1)
	start_and_end_with_1 = 10 ** (n - 2) if n > 1 else 0
	
	return start_with_1 + end_with_1 - start_and_end_with_1
