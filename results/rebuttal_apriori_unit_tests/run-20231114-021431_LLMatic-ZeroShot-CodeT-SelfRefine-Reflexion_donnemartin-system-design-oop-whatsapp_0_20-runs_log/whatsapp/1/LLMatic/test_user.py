import pytest
from user import UserService

@pytest.fixture

def user_service():
	return UserService()

def test_set_profile_picture_and_status(user_service):
	user_id = 1
	picture_path = '/path/to/picture.jpg'
	status_message = 'Hello, world!'
	assert user_service.set_profile(user_id, picture_path, status_message) == True

def test_privacy_settings(user_service):
	user_id = 1
	privacy_settings = 'Everyone'
	assert user_service.set_privacy(user_id, privacy_settings) == True
