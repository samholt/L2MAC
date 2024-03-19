def sort_array(array):
	"""
	Given an array of non-negative integers, return a copy of the given array after sorting,
	you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
	or sort it in descending order if the sum( first index value, last index value) is even.

	Note:
	* don't change the given array.

	Examples:
	* sort_array([]) => []
	* sort_array([5]) => [5]
	* sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
	* sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
	"""
	# Copy the array to avoid changing the original
	array_copy = array.copy()

	# Check if the array is empty or contains only one element
	if len(array_copy) < 2:
		return array_copy

	# Calculate the sum of the first and last index values
	sum_of_first_and_last = array_copy[0] + array_copy[-1]

	# Sort the array in ascending order if the sum is odd
	if sum_of_first_and_last % 2 == 1:
		array_copy.sort()
	# Sort the array in descending order if the sum is even
	else:
		array_copy.sort(reverse=True)

	return array_copy
