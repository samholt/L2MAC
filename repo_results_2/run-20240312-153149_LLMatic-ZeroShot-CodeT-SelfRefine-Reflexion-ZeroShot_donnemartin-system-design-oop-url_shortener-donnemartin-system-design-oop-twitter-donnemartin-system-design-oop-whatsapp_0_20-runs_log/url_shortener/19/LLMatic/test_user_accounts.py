import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()

	# Test registration
	assert user_accounts.register('user1', 'password1') == 'User registered successfully'
	assert user_accounts.register('user1', 'password1') == 'Username already exists'

	# Test login
	assert user_accounts.login('user1', 'password1') == 'Logged in successfully'
	assert user_accounts.login('user1', 'wrong_password') == 'Invalid username or password'
	assert user_accounts.login('non_existent_user', 'password1') == 'Invalid username or password'

	# Test URL management
	assert user_accounts.add_url('user1', 'url1') == 'URL added successfully'
	assert user_accounts.view_urls('user1') == ['url1']
	assert user_accounts.edit_url('user1', 'url1', 'url2') == 'URL edited successfully'
	assert user_accounts.view_urls('user1') == ['url2']
	assert user_accounts.delete_url('user1', 'url2') == 'URL deleted successfully'
	assert user_accounts.view_urls('user1') == []
