def is_simple_power(x, n):
	"""Checks if a number x is a simple power of n.

	A number x is a simple power of n if there exists an integer i such that n raised to the power of i equals x.
	In other words, if n**i equals x for some integer i, then x is a simple power of n.

	Args:
		x (int): The number to check.
		n (int): The base number.

	Returns:
		bool: True if x is a simple power of n, False otherwise.
	"""
	if x == 1:
		return True
	i = 0
	while n ** i <= x:
		if n ** i == x:
			return True
		i += 1
	return False
