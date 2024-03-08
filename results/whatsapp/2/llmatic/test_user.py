import pytest
from user import User

def test_user_creation():
	user = User('test@example.com', 'password')
	assert user.email == 'test@example.com'
	assert user.password == 'password'


def test_set_profile_picture():
	user = User('test@example.com', 'password')
	user.set_profile_picture('picture.jpg')
	assert user.profile_picture == 'picture.jpg'


def test_set_status_message():
	user = User('test@example.com', 'password')
	user.set_status_message('Hello, world!')
	assert user.status_message == 'Hello, world!'


def test_set_privacy_settings():
	user = User('test@example.com', 'password')
	user.set_privacy_settings('last_seen', 'nobody')
	assert user.privacy_settings['last_seen'] == 'nobody'
