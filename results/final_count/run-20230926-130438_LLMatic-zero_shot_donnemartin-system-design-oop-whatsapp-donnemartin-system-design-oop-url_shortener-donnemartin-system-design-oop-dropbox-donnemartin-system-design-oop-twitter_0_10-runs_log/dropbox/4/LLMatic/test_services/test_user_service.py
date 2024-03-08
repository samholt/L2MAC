import pytest
from services.user_service import register_user, login_user, forgot_password

def test_register_user():
	user = register_user('Test User', 'test@example.com', 'password', 'profile.jpg')
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
	assert user.password == 'password'
	assert user.profile_picture == 'profile.jpg'
	assert user.storage_used == 0

def test_login_user():
	user = login_user('test@example.com', 'password')
	assert user is not None

def test_forgot_password():
	assert forgot_password('test@example.com', 'new_password') == True
	user = login_user('test@example.com', 'new_password')
	assert user is not None
