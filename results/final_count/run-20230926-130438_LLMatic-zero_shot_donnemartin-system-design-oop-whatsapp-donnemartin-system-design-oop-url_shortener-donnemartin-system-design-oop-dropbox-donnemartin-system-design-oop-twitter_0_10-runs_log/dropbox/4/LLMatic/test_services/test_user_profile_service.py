import pytest
from services.user_service import register_user, get_user_profile, change_password


def test_get_user_profile():
	user = register_user('Test User', 'test@example.com', 'password', 'profile.jpg')
	profile = get_user_profile('test@example.com')
	assert profile == user


def test_change_password():
	user = register_user('Test User', 'test@example.com', 'password', 'profile.jpg')
	assert change_password('test@example.com', 'password', 'new_password') == True
	assert change_password('test@example.com', 'wrong_password', 'new_password') == False
