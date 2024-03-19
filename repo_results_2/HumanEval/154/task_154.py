def cycpattern_check(a , b):
	"""You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
	cycpattern_check("abcd","abd") => False
	cycpattern_check("hello","ell") => True
	cycpattern_check("whassup","psus") => False
	cycpattern_check("abab","baa") => True
	cycpattern_check("efef","eeff") => False
	cycpattern_check("himenss","simen") => True
	"""

	# Check if b is a substring of a
	if b in a:
		return True

	# If b is not a substring of a, check all rotations of b
	for i in range(len(b)):
		# Rotate b by one character to the right
		b = b[-1] + b[:-1]

		# Check if the rotated string is a substring of a
		if b in a:
			return True

	# If none of the rotations is a substring of a, return False
	return False
