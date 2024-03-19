def add_elements(arr, k):
	"""
	Given a non-empty array of integers arr and an integer k, return
	the sum of the elements with at most two digits from the first k elements of arr.

	Example:

		Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
		Output: 24 # sum of 21 + 3

	Constraints:
		1. 1 <= len(arr) <= 100
		2. 1 <= k <= len(arr)
	"""
	if not 1 <= len(arr) <= 100:
		raise ValueError('The length of arr should be between 1 and 100.')
	if not 1 <= k <= len(arr):
		raise ValueError('k should be between 1 and the length of arr.')

	return sum([x for x in arr[:k] if -10 < x < 100])
