def next_smallest(lst):
	"""
	You are given a list of integers.
	Write a function next_smallest() that returns the 2nd smallest element of the list.
	Return None if there is no such element.
	
	next_smallest([1, 2, 3, 4, 5]) == 2
	next_smallest([5, 1, 4, 3, 2]) == 2
	next_smallest([]) == None
	next_smallest([1, 1]) == None
	"""
	if len(lst) < 2:
		return None
	
	lst = sorted(lst)
	first_min = second_min = None
	
	for num in lst:
		if first_min is None or num < first_min:
			second_min = first_min
			first_min = num
		elif num > first_min and (second_min is None or num < second_min):
			second_min = num
	
	return second_min if second_min is not None else None
