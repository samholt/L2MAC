import pytest
from auth import register_user, recover_password, set_profile_picture, set_status_message, set_privacy_settings


def test_register_user():
	user = register_user('test@example.com', 'password')
	assert user.email == 'test@example.com'
	assert user.password == 'password'


def test_recover_password():
	user = register_user('test2@example.com', 'password')
	assert recover_password('test2@example.com') == 'password'


def test_set_profile_picture():
	user = register_user('test3@example.com', 'password')
	set_profile_picture('test3@example.com', 'picture.jpg')
	assert user.profile_picture == 'picture.jpg'


def test_set_status_message():
	user = register_user('test4@example.com', 'password')
	set_status_message('test4@example.com', 'Hello, world!')
	assert user.status_message == 'Hello, world!'


def test_set_privacy_settings():
	user = register_user('test5@example.com', 'password')
	set_privacy_settings('test5@example.com', {'last_seen': 'friends'})
	assert user.privacy_settings == {'last_seen': 'friends'}
