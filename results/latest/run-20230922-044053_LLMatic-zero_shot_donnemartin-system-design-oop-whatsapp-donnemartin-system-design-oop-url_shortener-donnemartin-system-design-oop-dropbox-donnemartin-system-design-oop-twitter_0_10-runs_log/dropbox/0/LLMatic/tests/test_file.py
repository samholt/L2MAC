import pytest
from models.file import File
from models.user import User


def test_file():
	user = User('Test User', 'test@example.com', 'password')
	file = File('Test File', 'text', 1.0, '/path/to/file', user)

	assert file.get_name() == 'Test File'
	assert file.get_type() == 'text'
	assert file.get_size() == 1.0
	assert file.get_path() == '/path/to/file'
	assert file.get_owner() == user

	file.set_name('New Test File')
	file.set_type('pdf')
	file.set_size(2.0)
	file.set_path('/new/path/to/file')
	file.set_owner(None)

	assert file.get_name() == 'New Test File'
	assert file.get_type() == 'pdf'
	assert file.get_size() == 2.0
	assert file.get_path() == '/new/path/to/file'
	assert file.get_owner() == None
