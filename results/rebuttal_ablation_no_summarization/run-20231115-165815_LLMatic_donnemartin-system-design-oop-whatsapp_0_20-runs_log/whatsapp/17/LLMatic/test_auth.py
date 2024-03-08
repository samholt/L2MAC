import pytest
from auth import Auth


def test_signup():
	auth = Auth()
	assert auth.signup('user1', 'pass1') == True


def test_validate_user():
	auth = Auth()
	auth.signup('user1', 'pass1')
	assert auth.validate_user('user1', 'pass1') == True
	assert auth.validate_user('user1', 'wrong_pass') == False
	assert auth.validate_user('wrong_user', 'pass1') == False
