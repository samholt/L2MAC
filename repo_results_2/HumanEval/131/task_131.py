def digits(n):
	"""Given a positive integer n, return the product of the odd digits.
	Return 0 if all digits are even.
	For example:
	digits(1)  == 1
	digits(4)  == 0
	digits(235) == 15
	"""
	# Convert the integer to a string to be able to iterate over the digits
	n_str = str(n)
	# Initialize the product to 1
	product = 1
	# Initialize a flag to check if there are any odd digits
	odd_exists = False
	# Iterate over the digits
	for digit in n_str:
		# Convert the digit back to an integer
		digit = int(digit)
		# Check if the digit is odd
		if digit % 2 != 0:
			# If it is, multiply the product by the digit and set the flag to True
			product *= digit
			odd_exists = True
	# If there are no odd digits, return 0
	if not odd_exists:
		return 0
	# Otherwise, return the product
	return product
