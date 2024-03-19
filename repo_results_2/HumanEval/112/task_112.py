def reverse_delete(s,c):
	"""Task
	We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
	then check if the result string is palindrome.
	A string is called palindrome if it reads the same backward as forward.
	You should return a tuple containing the result string and True/False for the check.
	Example
	For s = "abcde", c = "ae", the result should be ('bcd',False)
	For s = "abcdef", c = "b"  the result should be ('acdef',False)
	For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
	"""

	# Create a new string that is a copy of s but with all characters that are present in c removed
	new_s = ''.join([char for char in s if char not in c])

	# Check if the new string is a palindrome
	is_palindrome = new_s == new_s[::-1]

	return (new_s, is_palindrome)
