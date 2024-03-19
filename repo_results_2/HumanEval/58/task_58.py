def common(l1: list, l2: list):
	"""Return sorted unique common elements for two lists.
	>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
	[1, 5, 653]
	>>> common([5, 3, 2, 8], [3, 2])
	[2, 3]
	"""
	# Convert the lists to sets to remove duplicates
	set1 = set(l1)
	set2 = set(l2)
	# Find the intersection of the two sets
	common_elements = set1 & set2
	# Convert the resulting set to a list and sort it
	return sorted(list(common_elements))

def test_common():
	assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
	assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
	assert common([1, 2, 3], [4, 5, 6]) == []
	assert common([], []) == []
