def count_distinct_characters(string: str) -> int:
	""" Given a string, find out how many distinct characters (regardless of case) does it consist of
	>>> count_distinct_characters('xyzXYZ')
	3
	>>> count_distinct_characters('Jerry')
	4
	"""
	# Convert the string to lowercase
	lowercase_string = string.lower()
	# Convert the string to a set to remove duplicates
	distinct_characters = set(lowercase_string)
	# Return the number of distinct characters
	return len(distinct_characters)
