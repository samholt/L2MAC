import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()

	# Test creating an account
	assert user_accounts.create_account('testuser') == 'Account created successfully.'
	assert user_accounts.create_account('testuser') == 'Username already exists.'

	# Test getting URLs for a user
	assert user_accounts.get_urls('testuser') == []
	assert user_accounts.get_urls('nonexistentuser') == 'Username does not exist.'

	# Test adding a URL for a user
	assert user_accounts.add_url('testuser', 'testurl') == 'URL added successfully.'
	assert user_accounts.get_urls('testuser') == ['testurl']

	# Test editing a URL for a user
	assert user_accounts.edit_url('testuser', 'testurl', 'newurl') == 'URL edited successfully.'
	assert user_accounts.get_urls('testuser') == ['newurl']

	# Test deleting a URL for a user
	assert user_accounts.delete_url('testuser', 'newurl') == 'URL deleted successfully.'
	assert user_accounts.get_urls('testuser') == []

	# Test deleting a user
	assert user_accounts.delete_user('testuser') == 'User deleted successfully.'
	assert user_accounts.delete_user('testuser') == 'Username does not exist.'
