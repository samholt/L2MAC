import pytest
from user import User

def test_user_registration():
	user = User('test_user', 'test_password')
	user.register()
	assert user.username == 'test_user'
	assert user.password == 'test_password'

def test_user_login():
	user = User('test_user', 'test_password')
	user.login()
	# Add assertions for login

def test_user_logout():
	user = User('test_user', 'test_password')
	user.logout()
	# Add assertions for logout

def test_get_files():
	user = User('test_user', 'test_password')
	files = user.get_files()
	# Add assertions for get_files
