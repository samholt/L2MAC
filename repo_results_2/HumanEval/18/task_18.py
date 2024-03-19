def how_many_times(string: str, substring: str) -> int:
	""" Find how many times a given substring can be found in the original string. Count overlapping cases.

	Args:
		string (str): The original string.
		substring (str): The substring to be found in the original string.

	Returns:
		int: The number of times the substring occurs in the original string, including overlapping cases.

	Examples:
		>>> how_many_times('', 'a')
		0
		>>> how_many_times('aaa', 'a')
		3
		>>> how_many_times('aaaa', 'aa')
		3
	"""
	return len([i for i in range(len(string)) if string.startswith(substring, i)])
