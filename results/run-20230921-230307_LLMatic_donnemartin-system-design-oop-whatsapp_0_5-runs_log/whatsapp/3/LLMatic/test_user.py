import pytest
from user import User

def test_user_registration():
	user = User('test@example.com', 'password')
	assert user.register('test2@example.com', 'password2') == True


def test_user_authentication():
	user = User('test@example.com', 'password')
	assert user.authenticate('test@example.com', 'password') == True


def test_set_profile_picture():
	user = User('test@example.com', 'password')
	assert user.set_profile_picture('picture.jpg') == True


def test_set_status_message():
	user = User('test@example.com', 'password')
	assert user.set_status_message('Hello, world!') == True


def test_manage_privacy_settings():
	user = User('test@example.com', 'password')
	assert user.manage_privacy_settings({'last_seen': 'contacts_only'}) == True


def test_manage_contacts():
	user = User('test@example.com', 'password')
	assert user.manage_contacts('contact@example.com') == True
