import pytest
from user import User, UserManager


def test_user_creation():
	user = User('test', 'password', 'test@test.com')
	assert user.username == 'test'
	assert user.email == 'test@test.com'
	assert user.check_password('password')


def test_user_manager():
	user_manager = UserManager()
	assert user_manager.create_user('test', 'password', 'test@test.com')
	assert user_manager.create_user('test', 'password', 'test@test.com') is None
	assert user_manager.get_user('test').check_password('password')
	assert not user_manager.get_user('test').check_password('wrong_password')
