import pytest
from models.file_version import FileVersion
from models.file import File
from models.user import User


def test_file_version():
	user = User('Test User', 'test@example.com', 'password')
	file = File('Test File', 'text', 1.0, '/path/to/file', user)
	file_version = FileVersion(file, 1)

	assert file_version.get_file() == file
	assert file_version.get_version_number() == 1

	file_version.set_file(None)
	file_version.set_version_number(2)

	assert file_version.get_file() == None
	assert file_version.get_version_number() == 2
