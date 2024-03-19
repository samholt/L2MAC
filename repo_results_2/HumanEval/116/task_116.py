def sort_array(arr):
	"""
	In this Kata, you have to sort an array of non-negative integers according to
	number of ones in their binary representation in ascending order.
	For similar number of ones, sort based on decimal value.

	It must be implemented like this:
	>>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
	>>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
	>>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
	"""

	if not isinstance(arr, list):
		raise TypeError('Input should be a list')

	for i in arr:
		if not isinstance(i, int) or i < 0:
			raise ValueError('All elements in the list should be non-negative integers')

	return sorted(arr, key=lambda x: (bin(x).count('1'), x))
