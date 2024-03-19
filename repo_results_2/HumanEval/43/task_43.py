def pairs_sum_to_zero(l):
	"""
	pairs_sum_to_zero takes a list of integers as an input.
	it returns True if there are two distinct elements in the list that
	sum to zero, and False otherwise.
	"""
	# Create a set to store the elements of the list
	elements = set(l)

	# Iterate over the list
	for element in l:
		# Check if the negation of the current element is in the set
		if -element in elements and element != 0:
			# If it is, return True
			return True

	# If no such pair is found after iterating over the list, return False
	return False
