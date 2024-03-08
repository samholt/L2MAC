import pytest
from user import User
from file import File


def test_user():
	user = User('username', 'password')
	assert user.username == 'username'
	assert user.password == 'password'
	assert user.files == []

	file = File('file_name', 'file_size', 'file_type', 'file_content')
	user.upload_file(file)
	assert file in user.files

	assert user.view_file('file_name') is not None
	assert user.search_file('file_name') is not None

	user.share_file('file_name', 'other_user')
	assert user.download_file('file_name') is not None
