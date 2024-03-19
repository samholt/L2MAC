def is_palindrome(string: str) -> bool:
	""" Test if given string is a palindrome """
	return string == string[::-1]


def make_palindrome(string: str) -> str:
	""" Find the shortest palindrome that begins with a supplied string.
	Algorithm idea is simple:
	- Find the longest postfix of supplied string that is a palindrome.
	- Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
	"""
	i = len(string)
	while i > 0:
		if is_palindrome(string[:i]):
			break
		i -= 1
	return string + string[i-1::-1]


# Test cases
assert make_palindrome('') == ''
assert make_palindrome('cat') == 'catac'
assert make_palindrome('cata') == 'catac'
