import pytest
from user import User

def test_user_creation():
	user = User('test_user', 'test_password', 'test_email')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.email == 'test_email'


def test_user_update():
	user = User('test_user', 'test_password', 'test_email')
	user.update_user(username='updated_user', password='updated_password', email='updated_email')
	assert user.username == 'updated_user'
	assert user.password == 'updated_password'
	assert user.email == 'updated_email'


def test_user_deletion():
	user = User('test_user', 'test_password', 'test_email')
	user.delete_user()
	assert user.username == None
	assert user.password == None
	assert user.email == None
