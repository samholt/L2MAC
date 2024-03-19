def median(l: list):
	"""Return median of elements in the list l.
	>>> median([3, 1, 2, 4, 5])
	3
	>>> median([-10, 4, 6, 1000, 10, 20])
	15.0
	"""
	l.sort()
	length = len(l)
	if length % 2 == 0:
		return (l[length // 2] + l[length // 2 - 1]) / 2
	else:
		return l[length // 2]
