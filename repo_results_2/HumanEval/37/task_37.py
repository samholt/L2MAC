def sort_even(l: list):
	"""This function takes a list l and returns a list l' such that
	l' is identical to l in the odd indicies, while its values at the even indicies are equal
	to the values of the even indicies of l, but sorted.
	>>> sort_even([1, 2, 3])
	[1, 2, 3]
	>>> sort_even([5, 6, 3, 4])
	[3, 6, 5, 4]
	"""
	even_indices = []
	odd_indices = []
	for i, value in enumerate(l):
		if i % 2 == 0:
			even_indices.append(value)
		else:
			odd_indices.append(value)
	even_indices.sort()
	l_prime = [None]*(len(even_indices)+len(odd_indices))
	l_prime[::2] = even_indices
	l_prime[1::2] = odd_indices
	return l_prime
