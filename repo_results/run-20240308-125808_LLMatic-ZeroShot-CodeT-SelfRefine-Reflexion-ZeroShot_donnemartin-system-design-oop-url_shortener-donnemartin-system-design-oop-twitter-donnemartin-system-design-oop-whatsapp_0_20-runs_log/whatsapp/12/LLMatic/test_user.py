import pytest
from user import User, sign_up, recover_password, mock_db

def test_user_creation():
	user = User('test@test.com', 'password', 'profile_picture.jpg', 'Hello, world!', 'private')
	assert user.email == 'test@test.com'
	assert user.password == 'password'
	assert user.profile_picture == 'profile_picture.jpg'
	assert user.status_message == 'Hello, world!'
	assert user.privacy == 'private'

def test_sign_up():
	assert sign_up('test@test.com', 'password', 'profile_picture.jpg', 'Hello, world!', 'private') == 'User created successfully'
	assert sign_up('test@test.com', 'password') == 'User already exists'

def test_recover_password():
	assert recover_password('test@test.com') == 'Password reset successful'
	assert recover_password('nonexistent@test.com') == 'User does not exist'
