def file_name_check(file_name):
	"""Create a function which takes a string representing a file's name, and returns
	'Yes' if the the file's name is valid, and returns 'No' otherwise.
	A file's name is considered to be valid if and only if all the following conditions 
	are met:
	- There should not be more than three digits ('0'-'9') in the file's name.
	- The file's name contains exactly one dot '.'
	- The substring before the dot should not be empty, and it starts with a letter from 
	the latin alphapet ('a'-'z' and 'A'-'Z').
	- The substring after the dot should be one of these: ['txt', 'exe', 'dll']
	Examples:
	file_name_check("example.txt") # => 'Yes'
	file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
	"""
	valid_extensions = ['txt', 'exe', 'dll']
	file_parts = file_name.split('.')
	
	# Check if file name contains more than three digits
	if sum(c.isdigit() for c in file_name) > 3:
		return 'No'
	
	# Check if file name contains exactly one dot
	if file_name.count('.') != 1:
		return 'No'
	
	# Check if the substring before the dot is not empty and starts with a latin alphabet letter
	if not file_parts[0] or not file_parts[0][0].isalpha():
		return 'No'
	
	# Check if the substring after the dot is one of the valid extensions
	if file_parts[1] not in valid_extensions:
		return 'No'
	
	return 'Yes'
