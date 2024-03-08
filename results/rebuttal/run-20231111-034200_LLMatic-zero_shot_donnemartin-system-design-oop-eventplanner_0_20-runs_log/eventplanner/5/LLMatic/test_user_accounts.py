import pytest
from user_accounts import User

def test_user_creation():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'


def test_profile_management():
	user = User('test_user', 'test_password')
	user.create_profile({'name': 'Test User', 'email': 'test@example.com'})
	assert user.get_profile() == {'name': 'Test User', 'email': 'test@example.com'}
	user.update_profile({'phone': '1234567890'})
	assert user.get_profile() == {'name': 'Test User', 'email': 'test@example.com', 'phone': '1234567890'}


def test_event_preferences():
	user = User('test_user', 'test_password')
	user.set_event_preferences({'theme': 'Business', 'location': 'Online'})
	assert user.get_event_preferences() == {'theme': 'Business', 'location': 'Online'}
