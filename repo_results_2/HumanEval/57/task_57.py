def monotonic(l: list) -> bool:
	"""Return True if list elements are monotonically increasing or decreasing.
	
	Args:
		l (list): The list to check.
	
	Returns:
		bool: True if the list is monotonically increasing or decreasing, False otherwise.
	"""
	if len(l) <= 1:
		return True
	
	is_increasing = l[1] >= l[0]
	
	for i in range(2, len(l)):
		if (is_increasing and l[i] < l[i-1]) or (not is_increasing and l[i] > l[i-1]):
			return False
	
	return True
