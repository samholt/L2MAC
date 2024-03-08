import file_management

def test_upload_file():
	file = file_management.File('test', 'txt', 500, 'Hello, world!')
	assert file_management.upload_file(file) == 'File uploaded successfully'
	assert file_management.mock_db['test'] == file

	file = file_management.File('test', 'exe', 500, 'Hello, world!')
	assert file_management.upload_file(file) == 'File type not allowed'

	file = file_management.File('test', 'txt', 1000001, 'Hello, world!')
	assert file_management.upload_file(file) == 'File size exceeds limit'

def test_download_file():
	file = file_management.File('test', 'txt', 500, 'Hello, world!')
	file_management.mock_db['test'] = file
	assert file_management.download_file('test') == 'Hello, world!'
	assert file_management.download_file('nonexistent') == None
