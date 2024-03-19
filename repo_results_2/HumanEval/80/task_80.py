def is_happy(s):
	"""You are given a string s.
	Your task is to check if the string is happy or not.
	A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
	For example:
	is_happy(a) => False
	is_happy(aa) => False
	is_happy(abcd) => True
	is_happy(aabb) => False
	is_happy(adb) => True
	is_happy(xyy) => False
	"""
	# Check if the length of the string is less than 3
	if len(s) < 3:
		return False
	# Iterate over the string with a step of 3
	for i in range(0, len(s)-2):
		# Check if the current character and the next two characters are distinct
		if len(set(s[i:i+3])) != 3:
			return False
	# If all 3 consecutive characters are distinct, return True
	return True
