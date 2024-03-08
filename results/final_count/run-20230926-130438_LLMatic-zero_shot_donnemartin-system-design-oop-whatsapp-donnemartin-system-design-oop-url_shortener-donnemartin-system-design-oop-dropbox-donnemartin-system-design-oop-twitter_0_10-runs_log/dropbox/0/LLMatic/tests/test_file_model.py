from models.File import File

def test_file_model():
	file = File('1', 'file1', 'txt', 100, '/path/to/file', 'user1', ['v1', 'v2'])
	assert file.id == '1'
	assert file.name == 'file1'
	assert file.type == 'txt'
	assert file.size == 100
	assert file.path == '/path/to/file'
	assert file.user == 'user1'
	assert file.tags == ['v1', 'v2']
