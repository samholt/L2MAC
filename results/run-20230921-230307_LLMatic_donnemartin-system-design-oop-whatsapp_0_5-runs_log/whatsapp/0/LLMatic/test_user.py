import pytest
from user import User

def test_user_registration():
	user = User()
	user.register('test@example.com', 'password')
	assert user.email == 'test@example.com'
	assert user.password == 'password'

def test_user_login():
	user = User()
	user.register('test@example.com', 'password')
	assert user.login('test@example.com', 'password')
	assert not user.login('wrong@example.com', 'password')

def test_password_recovery():
	user = User()
	user.register('test@example.com', 'password')
	assert user.recover_password('test@example.com') == 'password'
	assert user.recover_password('wrong@example.com') is None

def test_profile_picture_setting():
	user = User()
	user.set_profile_picture('picture.jpg')
	assert user.profile_picture == 'picture.jpg'

def test_status_message_setting():
	user = User()
	user.set_status_message('Hello, world!')
	assert user.status_message == 'Hello, world!'

def test_privacy_settings_setting():
	user = User()
	user.set_privacy_settings('Private')
	assert user.privacy_settings == 'Private'

def test_contact_blocking():
	user = User()
	user.block_contact('contact1')
	assert 'contact1' in user.blocked_contacts
	user.unblock_contact('contact1')
	assert 'contact1' not in user.blocked_contacts
