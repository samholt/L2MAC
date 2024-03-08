import pytest
from profile import Profile
from user import User


def test_profile_creation():
	user = User('test@example.com', 'password')
	profile = Profile(user)
	assert profile.user == user
	assert profile.profile_picture is None
	assert profile.status_message is None
	assert profile.privacy_settings == {}


def test_set_profile_picture():
	user = User('test@example.com', 'password')
	profile = Profile(user)
	profile.set_profile_picture('picture.jpg')
	assert profile.profile_picture == 'picture.jpg'


def test_set_status_message():
	user = User('test@example.com', 'password')
	profile = Profile(user)
	profile.set_status_message('Hello, world!')
	assert profile.status_message == 'Hello, world!'


def test_manage_privacy_settings():
	user = User('test@example.com', 'password')
	profile = Profile(user)
	privacy_settings = {'last_seen': 'only_me'}
	profile.manage_privacy_settings(privacy_settings)
	assert profile.privacy_settings == privacy_settings
