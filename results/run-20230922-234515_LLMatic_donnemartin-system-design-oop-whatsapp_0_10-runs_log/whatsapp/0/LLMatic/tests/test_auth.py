import pytest
from services.auth import register_user, set_profile_picture, set_status_message, set_privacy_settings

def test_set_profile_picture():
	user = register_user('test@example.com', 'password')
	user = set_profile_picture(user.id, 'new_picture.jpg')
	assert user.profile_picture == 'new_picture.jpg'

def test_set_status_message():
	user = register_user('test@example.com', 'password')
	user = set_status_message(user.id, 'Hello, world!')
	assert user.status_message == 'Hello, world!'

def test_set_privacy_settings():
	user = register_user('test@example.com', 'password')
	user = set_privacy_settings(user.id, {'last_seen_status': 'friends_only'})
	assert user.privacy_settings == {'last_seen_status': 'friends_only'}
