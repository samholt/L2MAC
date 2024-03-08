import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()

	# Test creating account
	assert user_accounts.create_account('user1', 'password1') == 'Account created successfully'
	assert user_accounts.create_account('user1', 'password2') == 'Username already exists'

	# Test customizing profile
	assert user_accounts.customize_profile('user1', {'name': 'User One', 'preferences': 'Outdoor events'}) == 'Profile updated successfully'
	assert user_accounts.customize_profile('user2', {'name': 'User Two'}) == 'User not found'

	# Test saving and accessing events
	assert user_accounts.save_event('user1', 'Event1', 'past') == 'Event saved successfully'
	assert user_accounts.save_event('user1', 'Event2', 'upcoming') == 'Event saved successfully'
	assert user_accounts.save_event('user2', 'Event3', 'past') == 'User not found'
	assert user_accounts.get_events('user1', 'past') == ['Event1']
	assert user_accounts.get_events('user1', 'upcoming') == ['Event2']
	assert user_accounts.get_events('user2', 'past') == 'User not found'
