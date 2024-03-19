def total_match(lst1, lst2):
	''' 
	This function accepts two lists of strings and returns the list that has 
	total number of chars in the all strings of the list less than the other list.

	If the two lists have the same number of chars, it returns the first list.
	'''

	# If both lists are empty, return an empty list
	if not lst1 and not lst2:
		return []

	# Calculate the total number of characters in each list
	total_chars_lst1 = sum([len(str) for str in lst1])
	total_chars_lst2 = sum([len(str) for str in lst2])

	# Compare the total number of characters in each list and return the appropriate list
	if total_chars_lst1 <= total_chars_lst2:
		return lst1
	else:
		return lst2
