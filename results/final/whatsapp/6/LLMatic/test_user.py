import pytest
from user import User

def test_user():
	db = {}
	user = User('test@example.com', 'password')
	assert user.sign_up(db) == 'User registered successfully'
	assert user.sign_up(db) == 'User already exists'
	assert user.recover_password(db) == 'password'
	assert user.set_profile_picture('picture.jpg') == 'Profile picture updated successfully'
	assert user.set_status_message('Hello, world!') == 'Status message updated successfully'
	assert user.set_privacy_settings('Private') == 'Privacy settings updated successfully'
