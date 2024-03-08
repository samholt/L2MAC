import pytest
from user import User
from file import File


def test_file():
	user = User('test_user', 'password')
	file = File('test_file', 'content', user)
	assert file.view() == 'content'
	file.edit('new_content')
	assert file.view() == 'new_content'
	user2 = User('test_user2', 'password')
	file.share(user2, 'view')
	assert file.check_permission(user2, 'view') == True
	assert file.download() == 'new_content'
