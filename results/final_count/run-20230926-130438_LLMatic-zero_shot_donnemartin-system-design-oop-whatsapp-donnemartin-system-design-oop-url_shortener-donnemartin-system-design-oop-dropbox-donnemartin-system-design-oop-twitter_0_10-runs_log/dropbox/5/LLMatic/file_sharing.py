def generate_shareable_link(file_name):
	# Mocking a database with an in-memory dictionary
	file_database = {
		'file1': 'http://localhost:5000/download/file1',
		'file2': 'http://localhost:5000/download/file2',
		'file3': 'http://localhost:5000/download/file3'
	}

	# Check if the file exists in the database
	if file_name in file_database:
		# Return the shareable link
		return file_database[file_name]
	else:
		# Return an error message
		return 'File not found.'
