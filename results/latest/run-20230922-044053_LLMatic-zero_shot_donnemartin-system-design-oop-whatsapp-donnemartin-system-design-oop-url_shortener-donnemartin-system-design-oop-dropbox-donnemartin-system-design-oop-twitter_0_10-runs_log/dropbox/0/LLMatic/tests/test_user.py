import pytest
from models.user import User


def test_user_creation():
	user = User('Test User', 'test@example.com', 'password')
	assert user.get_name() == 'Test User'
	assert user.get_email() == 'test@example.com'
	assert user.get_password() == 'password'
	assert user.get_profile_picture() is None
	assert user.get_storage_used() == 0.0

def test_user_modification():
	user = User('Test User', 'test@example.com', 'password')
	user.set_name('New Name')
	user.set_email('new@example.com')
	user.set_password('newpassword')
	user.set_profile_picture('picture.jpg')
	user.set_storage_used(100.0)
	assert user.get_name() == 'New Name'
	assert user.get_email() == 'new@example.com'
	assert user.get_password() == 'newpassword'
	assert user.get_profile_picture() == 'picture.jpg'
	assert user.get_storage_used() == 100.0
