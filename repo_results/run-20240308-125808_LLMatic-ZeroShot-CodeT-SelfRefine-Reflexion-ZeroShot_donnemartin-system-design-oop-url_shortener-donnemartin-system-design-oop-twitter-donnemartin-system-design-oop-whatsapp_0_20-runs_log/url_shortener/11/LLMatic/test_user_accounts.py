import pytest
from user_accounts import UserAccounts

def test_user_accounts():
	user_accounts = UserAccounts()

	# Test creating account
	assert user_accounts.create_account('test', 'password') == 'Account created successfully.'
	assert user_accounts.create_account('test', 'password') == 'Username already exists.'

	# Test adding URL
	assert user_accounts.add_url('test', 'password', 'http://example.com') == 'URL added successfully.'
	assert user_accounts.add_url('test', 'wrongpassword', 'http://example.com') == 'Invalid credentials.'

	# Test viewing URLs
	assert user_accounts.view_urls('test', 'password') == ['http://example.com']
	assert user_accounts.view_urls('test', 'wrongpassword') == 'Invalid credentials.'

	# Test deleting URL
	assert user_accounts.delete_url('test', 'password', 'http://example.com') == 'URL deleted successfully.'
	assert user_accounts.delete_url('test', 'password', 'http://example.com') == 'URL not found.'
	assert user_accounts.delete_url('test', 'wrongpassword', 'http://example.com') == 'Invalid credentials.'

	# Test viewing analytics
	assert user_accounts.view_analytics('test', 'password') == []
	assert user_accounts.view_analytics('test', 'wrongpassword') == 'Invalid credentials.'
