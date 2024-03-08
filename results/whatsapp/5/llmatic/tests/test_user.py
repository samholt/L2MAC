import pytest
from models.user import User


def test_online_status():
	user = User(id='user_id', email='user@example.com', password='password', profile_picture='profile_picture.jpg', status_message='Hello, world!', privacy_settings={}, blocked_contacts=[])
	assert user.online_status == False
	user.online_status = True
	assert user.online_status == True
