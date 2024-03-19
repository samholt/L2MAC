def search(lst):
	'''You are given a non-empty list of positive integers. Return the greatest integer that is greater than zero, and has a frequency greater than or equal to the value of the integer itself. The frequency of an integer is the number of times it appears in the list. If no such a value exist, return -1.
	Examples:
		search([4, 1, 2, 2, 3, 1]) == 2
		search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
		search([5, 5, 4, 4, 4]) == -1
	'''
	from collections import Counter
	# Count the frequency of each integer in the list
	freq = Counter(lst)
	# Initialize the maximum value to -1
	max_val = -1
	# Iterate over the frequency dictionary
	for key, value in freq.items():
		# Check if the frequency is greater than or equal to the integer and the integer is greater than max_val
		if value >= key and key > max_val:
			# Update max_val
			max_val = key
	# If max_val is still -1, return -1
	if max_val == -1:
		return -1
	# Otherwise, return max_val
	else:
		return max_val
