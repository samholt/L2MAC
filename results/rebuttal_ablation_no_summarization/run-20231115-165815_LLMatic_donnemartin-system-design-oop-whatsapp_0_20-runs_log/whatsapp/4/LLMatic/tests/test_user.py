import pytest
from models.user import User

def test_user_creation():
	user = User('1', 'test@example.com', 'password', 'profile_pic.jpg', 'Hello there!', 'public', [])
	assert user.id == '1'
	assert user.email == 'test@example.com'
	assert user.password == 'password'
	assert user.profile_picture == 'profile_pic.jpg'
	assert user.status_message == 'Hello there!'
	assert user.privacy_settings == 'public'
	assert user.blocked_contacts == []
