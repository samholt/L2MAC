def generate_integers(a, b):
	"""
	Given two positive integers a and b, return the even digits between a
	and b, in ascending order.

	For example:
	generate_integers(2, 8) => [2, 4, 6, 8]
	generate_integers(8, 2) => [2, 4, 6, 8]
	generate_integers(10, 14) => []
	"""
	# Identify the smaller and larger integers
	smaller = min(a, b)
	larger = max(a, b)

	# Generate a list of all even integers between the smaller and larger integers (inclusive)
	even_numbers = [i for i in range(smaller, larger + 1) if i % 2 == 0]

	# Sort the list of even numbers in ascending order
	even_numbers.sort()

	# Return the sorted list of even numbers
	return even_numbers
