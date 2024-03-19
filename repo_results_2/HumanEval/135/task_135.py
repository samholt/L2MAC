def can_arrange(arr):
	"""Create a function which returns the largest index of an element which
	is not greater than or equal to the element immediately preceding it. If
	no such element exists then return -1. The given array will not contain
	duplicate values.

	Examples:
	can_arrange([1,2,4,3,5]) = 3
	can_arrange([1,2,3]) = -1
	"""
	for i in range(1, len(arr)):
		if arr[i] < arr[i-1]:
			return i
	return -1

def test_can_arrange():
	assert can_arrange([1,2,4,3,5]) == 3
	assert can_arrange([1,2,3]) == -1
	assert can_arrange([5,4,3,2,1]) == 1
	assert can_arrange([1]) == -1
	assert can_arrange([]) == -1
