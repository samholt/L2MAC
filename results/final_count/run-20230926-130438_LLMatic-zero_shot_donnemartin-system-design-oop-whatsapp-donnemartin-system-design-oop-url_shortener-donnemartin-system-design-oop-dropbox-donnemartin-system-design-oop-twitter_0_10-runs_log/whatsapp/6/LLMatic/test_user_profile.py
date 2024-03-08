import pytest
from user import User


def test_set_profile_picture():
	user = User()
	user.sign_up('test@test.com', 'password')
	assert user.set_profile_picture('test@test.com', 'image_file') == 'Profile picture updated successfully'
	assert user.profile_pictures['test@test.com'] == 'image_file'


def test_set_status_message():
	user = User()
	user.sign_up('test@test.com', 'password')
	assert user.set_status_message('test@test.com', 'Hello, world!') == 'Status message updated successfully'
	assert user.status_messages['test@test.com'] == 'Hello, world!'


def test_set_privacy_settings():
	user = User()
	user.sign_up('test@test.com', 'password')
	assert user.set_privacy_settings('test@test.com', 'private') == 'Privacy settings updated successfully'
	assert user.privacy_settings['test@test.com'] == 'private'
