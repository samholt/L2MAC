import pytest
from user import User

def test_create_user():
	user = User('test', 'password')
	assert user.username == 'test'
	assert user.password == 'password'


def test_edit_user():
	user = User('test', 'password')
	user.edit_user('new_test', 'new_password')
	assert user.username == 'new_test'
	assert user.password == 'new_password'


def test_delete_user():
	user = User('test', 'password')
	user.delete_user()
	assert user.username == None
	assert user.password == None
	assert user.urls == []
