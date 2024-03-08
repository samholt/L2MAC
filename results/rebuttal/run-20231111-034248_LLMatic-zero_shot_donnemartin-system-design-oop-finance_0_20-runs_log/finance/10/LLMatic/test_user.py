import pytest
from user import User


def test_create_user():
	user = User()
	assert user.create_user('test', 'password') == 'User created successfully'
	assert user.create_user('test', 'password') == 'Username already exists'


def test_login():
	user = User()
	user.create_user('test', 'password')
	assert user.login('test', 'password') == 'Login successful'
	assert user.login('test', 'wrong_password') == 'Incorrect password'
	assert user.login('wrong_username', 'password') == 'Username does not exist'


def test_password_recovery():
	user = User()
	user.create_user('test', 'password')
	assert user.password_recovery('test') == 'Password recovery email sent'
	assert user.password_recovery('wrong_username') == 'Username does not exist'
