from file_management import File, upload_file, download_file, MAX_FILE_SIZE, ALLOWED_FILE_TYPES


def test_upload_download():
	file = File('test.txt', 'txt', 100, b'This is a test file', 1, '')
	assert upload_file(file) == 'File uploaded successfully'
	assert download_file('test.txt').name == 'test.txt'


def test_file_size_limit():
	file = File('big_file.txt', 'txt', MAX_FILE_SIZE + 1, b'This is a big file', 1, '')
	assert upload_file(file) == 'File size exceeds limit'


def test_file_type_restriction():
	file = File('test.exe', 'exe', 100, b'This is an executable file', 1, '')
	assert upload_file(file) == 'File type not allowed'


def test_file_not_found():
	assert download_file('non_existent.txt') == 'File not found'


def test_file_preview():
	file = File('test.txt', 'txt', 100, b'This is a test file', 1, '')
	upload_file(file)
	assert download_file('test.txt').preview == b'This is a test file'[:100]
