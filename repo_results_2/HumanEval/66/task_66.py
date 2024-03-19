def digitSum(s):
	"""Task
	Write a function that takes a string as input and returns the sum of the upper characters only'
	ASCII codes.

	Examples:
		digitSum("") => 0
		digitSum("abAB") => 131
		digitSum("abcCd") => 67
		digitSum("helloE") => 69
		digitSum("woArBld") => 131
		digitSum("aAaaaXa") => 153
	"""
	# Initialize a variable to store the sum
	sum_ascii = 0
	# Iterate over each character in the string
	for char in s:
		# Check if the character is uppercase
		if char.isupper():
			# If it is, add its ASCII value to the sum
			sum_ascii += ord(char)
	# Return the sum
	return sum_ascii
