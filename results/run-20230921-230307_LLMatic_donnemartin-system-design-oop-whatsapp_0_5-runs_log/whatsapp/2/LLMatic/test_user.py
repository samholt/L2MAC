import pytest
from user import User


def test_user_creation():
	user = User('test@example.com', 'password')
	assert user.email == 'test@example.com'
	assert user.password == 'password'


def test_user_sign_up():
	user = User(None, None)
	user.sign_up()
	assert user.email is not None
	assert user.password is not None


def test_user_log_in():
	user = User('test@example.com', 'password')
	assert user.log_in('test@example.com', 'password') is True
	assert user.log_in('wrong@example.com', 'password') is False


def test_recover_password():
	user = User('test@example.com', 'password')
	old_password = user.password
	user.recover_password()
	assert user.password != old_password
