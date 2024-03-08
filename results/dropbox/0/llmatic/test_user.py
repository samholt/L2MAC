import pytest
from user import User

def test_user_registration():
	user = User(1, 'test', 'password')
	assert user.register('test2', 'password2') == True
	assert user.register('test', 'password') == False

def test_user_login():
	user = User(1, 'test', 'password')
	assert user.login('test', 'password') == True
	assert user.login('test', 'wrongpassword') == False
	assert user.login('wronguser', 'password') == False

def test_user_logout():
	user = User(1, 'test', 'password')
	assert user.logout() == None

