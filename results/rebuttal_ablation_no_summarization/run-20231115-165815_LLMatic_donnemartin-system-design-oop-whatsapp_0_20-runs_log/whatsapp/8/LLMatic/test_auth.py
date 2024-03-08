import pytest
from auth import User

def test_user_signup():
	user = User('test@example.com', 'password')
	assert user.signup('test@example.com', 'password') == True


def test_user_login():
	user = User('test@example.com', 'password')
	assert user.login('test@example.com', 'password') == True
	assert user.login('wrong@example.com', 'password') == False


def test_recover_password():
	user = User('test@example.com', 'password')
	assert user.recover_password('test@example.com') == 'Password recovery email sent'
	assert user.recover_password('wrong@example.com') == 'Email not found'

