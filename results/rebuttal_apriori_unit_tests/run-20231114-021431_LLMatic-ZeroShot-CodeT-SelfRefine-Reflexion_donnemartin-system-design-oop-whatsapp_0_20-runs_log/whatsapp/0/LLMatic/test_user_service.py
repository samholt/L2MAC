import pytest
from user_service import UserService

@pytest.fixture

def user_service():
	return UserService()

def test_set_profile(user_service):
	assert user_service.set_profile(1, '/path/to/picture.jpg', 'Hello!') == True
	assert user_service.user_profiles[1] == {'picture_path': '/path/to/picture.jpg', 'status_message': 'Hello!'}

def test_set_privacy(user_service):
	assert user_service.set_privacy(1, 'Everyone') == True
	assert user_service.user_privacy[1] == 'Everyone'
