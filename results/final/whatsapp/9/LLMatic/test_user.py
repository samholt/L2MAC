import pytest
from user import User

def test_user_creation():
	user = User('test@test.com', 'password')
	assert user.email == 'test@test.com'
	assert user.password == 'password'


def test_sign_up():
	db = {}
	user = User('test@test.com', 'password')
	assert user.sign_up(db) == 'User created successfully'
	assert user.sign_up(db) == 'Email already exists'


def test_recover_password():
	user = User('test@test.com', 'password')
	assert user.recover_password() == 'Password recovery email sent'


def test_set_profile_picture():
	user = User('test@test.com', 'password')
	user.set_profile_picture('picture.jpg')
	assert user.profile_picture == 'picture.jpg'


def test_set_status_message():
	user = User('test@test.com', 'password')
	user.set_status_message('Hello World')
	assert user.status_message == 'Hello World'


def test_set_privacy_settings():
	user = User('test@test.com', 'password')
	user.set_privacy_settings('Private')
	assert user.privacy_settings == 'Private'


def test_set_connectivity():
	user = User('test@test.com', 'password')
	user.set_connectivity(False)
	assert user.connectivity == False
