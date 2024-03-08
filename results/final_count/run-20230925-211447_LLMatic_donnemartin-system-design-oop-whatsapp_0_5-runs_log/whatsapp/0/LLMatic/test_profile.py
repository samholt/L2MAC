import pytest
from profile import UserProfile

def test_set_profile_picture():
	user_profile = UserProfile()
	user_profile.set_profile_picture('test@example.com', 'picture.jpg')
	assert user_profile.user_profiles['test@example.com']['picture'] == 'picture.jpg'

def test_set_status_message():
	user_profile = UserProfile()
	user_profile.set_status_message('test@example.com', 'Hello, world!')
	assert user_profile.user_profiles['test@example.com']['status'] == 'Hello, world!'

def test_set_privacy_settings():
	user_profile = UserProfile()
	user_profile.set_privacy_settings('test@example.com', 'private')
	assert user_profile.user_profiles['test@example.com']['privacy'] == 'private'
