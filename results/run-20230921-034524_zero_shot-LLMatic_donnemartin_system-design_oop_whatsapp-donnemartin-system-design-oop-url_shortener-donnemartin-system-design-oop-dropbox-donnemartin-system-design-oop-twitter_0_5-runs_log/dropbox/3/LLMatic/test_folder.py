import pytest
from user import User
from file import File
from folder import Folder


def test_folder():
	user = User('test_user', 'password')
	folder = Folder('test_folder', user)
	file = File('test_file', 'content', user)
	folder.add_file(file)
	assert file in folder.files
	folder.remove_file(file)
	assert file not in folder.files
	user2 = User('test_user2', 'password')
	folder.grant_permission(user2, 'view')
	assert folder.check_permission(user2) == 'view'
	folder.revoke_permission(user2)
	assert folder.check_permission(user2) == None
