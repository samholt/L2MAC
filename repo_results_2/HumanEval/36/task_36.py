def fizz_buzz(n: int) -> int:
	"""Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
	
	Args:
		n (int): The upper limit of the range to check.
	
	Returns:
		int: The count of '7's in numbers divisible by 11 or 13.
	"""
	counter = 0
	for i in range(1, n):
		if i % 11 == 0 or i % 13 == 0:
			counter += str(i).count('7')
	return counter
