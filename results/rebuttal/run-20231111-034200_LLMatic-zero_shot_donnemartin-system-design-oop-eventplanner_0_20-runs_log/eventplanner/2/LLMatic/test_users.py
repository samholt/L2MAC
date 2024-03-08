import pytest
from users import create_user, get_user, update_user_profile, save_user_event, get_user_events

def test_create_user():
	assert create_user('testuser', 'password') == 'User created successfully'
	assert create_user('testuser', 'password') == 'User already exists'

def test_get_user():
	assert get_user('testuser').username == 'testuser'
	assert get_user('nonexistentuser') == 'User not found'

def test_update_user_profile():
	assert update_user_profile('testuser', {'name': 'Test User'}) == 'Profile updated successfully'
	assert update_user_profile('nonexistentuser', {'name': 'Test User'}) == 'User not found'

def test_save_user_event():
	assert save_user_event('testuser', 'Event1', 'upcoming') == 'Event saved successfully'
	assert save_user_event('nonexistentuser', 'Event1', 'upcoming') == 'User not found'

def test_get_user_events():
	assert get_user_events('testuser', 'upcoming') == ['Event1']
	assert get_user_events('nonexistentuser', 'upcoming') == 'User not found'
