import pytest
from user_accounts import UserAccounts

def test_create_account():
	user_accounts = UserAccounts()
	assert user_accounts.create_account('test') == 'Account created successfully.'
	assert user_accounts.create_account('test') == 'Username already exists.'

def test_view_urls():
	user_accounts = UserAccounts()
	user_accounts.create_account('test')
	assert user_accounts.view_urls('test') == []
	assert user_accounts.view_urls('nonexistent') == 'Username does not exist.'

def test_add_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('test')
	assert user_accounts.add_url('test', 'http://example.com') == 'URL added successfully.'
	assert user_accounts.view_urls('test') == ['http://example.com']

def test_delete_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('test')
	user_accounts.add_url('test', 'http://example.com')
	assert user_accounts.delete_url('test', 'http://example.com') == 'URL removed successfully.'
	assert user_accounts.view_urls('test') == []
