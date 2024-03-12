import pytest
from user import User

def test_user_creation():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.urls == []

def test_user_edit():
	user = User('test_user', 'test_password')
	user.edit_user('new_user', 'new_password')
	assert user.username == 'new_user'
	assert user.password == 'new_password'

def test_user_delete():
	user = User('test_user', 'test_password')
	user.delete_user()
	assert user.username == None
	assert user.password == None
	assert user.urls == []
