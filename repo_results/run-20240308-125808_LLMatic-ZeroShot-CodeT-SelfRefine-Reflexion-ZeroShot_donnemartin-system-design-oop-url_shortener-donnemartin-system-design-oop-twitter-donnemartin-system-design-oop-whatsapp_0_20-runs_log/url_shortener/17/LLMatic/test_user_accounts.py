import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()

	# Test creating an account
	assert user_accounts.create_account('user1') == 'Account created successfully.'
	assert user_accounts.create_account('user1') == 'Username already exists.'

	# Test adding a URL
	assert user_accounts.add_url('user1', 'url1') == 'URL added successfully.'
	assert user_accounts.add_url('user2', 'url1') == 'Username does not exist.'

	# Test viewing URLs
	assert user_accounts.view_urls('user1') == ['url1']
	assert user_accounts.view_urls('user2') == 'Username does not exist.'

	# Test deleting a URL
	assert user_accounts.delete_url('user1', 'url1') == 'URL removed successfully.'
	assert user_accounts.delete_url('user1', 'url1') == 'URL does not exist.'
	assert user_accounts.delete_url('user2', 'url1') == 'Username does not exist.'

	# Test editing a URL
	assert user_accounts.add_url('user1', 'url2') == 'URL added successfully.'
	assert user_accounts.edit_url('user1', 'url2', 'url3') == 'URL edited successfully.'
	assert user_accounts.edit_url('user1', 'url2', 'url3') == 'URL does not exist.'
	assert user_accounts.edit_url('user2', 'url2', 'url3') == 'Username does not exist.'
