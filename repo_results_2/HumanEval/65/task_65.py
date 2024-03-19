def circular_shift(x, shift):
	"""Circular shift the digits of the integer x, shift the digits right by shift
	and return the result as a string.
	If shift > number of digits, return digits reversed.
	>>> circular_shift(12, 1)
	"21"
	>>> circular_shift(12, 2)
	"12"
	"""
	# Convert the integer x into a string
	x_str = str(x)
	# If x is a single digit number or shift is zero, return x as a string without any changes
	if len(x_str) == 1 or shift == 0:
		return x_str
	# If shift is negative, perform a circular shift to the left
	elif shift < 0:
		return x_str[-shift:] + x_str[:-shift]
	# If shift is greater than the number of digits in x, return the digits of x reversed
	elif shift > len(x_str):
		return x_str[::-1]
	# Otherwise, perform a circular shift of the digits of x to the right by the number of places specified by shift
	else:
		return x_str[-shift:] + x_str[:-shift]
