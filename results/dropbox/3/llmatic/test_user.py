import pytest
from user import User
from file import File


def test_user():
	user = User('test_user', 'password')
	file = File('test_file', 'content', user)
	user.upload_file(file)
	assert user.view_file(file.id) == file
	assert user.search_file('test_file') == file
	user2 = User('test_user2', 'password')
	user.share_file(file.id, user2)
	assert user.download_file(file.id) == 'content'
	user.grant_permission(file.id)
	assert user.edit_file(file.id, 'new_content') == True
	assert user.view_file(file.id).content == 'new_content'
	user.revoke_permission(file.id)
	assert user.permissions[file.id] == False
