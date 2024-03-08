import pytest
from user import User
from file import File
from permission import Permission


def test_permission():
	user = User('test_user', 'password')
	file = File('test_file', 'content', user)
	permission = Permission(user, file)
	permission.grant_permission(user, file, 'view')
	assert permission.check_permission(user, file, 'view') == True
	permission.revoke_permission(user, file, 'view')
	assert permission.check_permission(user, file, 'view') == False
