import pytest
from user_accounts import UserAccount

def test_create_account():
	user_account = UserAccount()
	assert user_account.create_account('test', 'password') == 'Account created successfully.'
	assert user_account.create_account('test', 'password') == 'Username already exists.'

def test_view_urls():
	user_account = UserAccount()
	user_account.create_account('test', 'password')
	assert user_account.view_urls('test') == []
	assert user_account.view_urls('nonexistent') == 'Username does not exist.'

def test_add_url():
	user_account = UserAccount()
	user_account.create_account('test', 'password')
	assert user_account.add_url('test', 'http://example.com') == 'URL added successfully.'
	assert user_account.add_url('nonexistent', 'http://example.com') == 'Username does not exist.'

def test_delete_url():
	user_account = UserAccount()
	user_account.create_account('test', 'password')
	user_account.add_url('test', 'http://example.com')
	assert user_account.delete_url('test', 'http://example.com') == 'URL removed successfully.'
	assert user_account.delete_url('test', 'http://nonexistent.com') == 'URL does not exist.'
	assert user_account.delete_url('nonexistent', 'http://example.com') == 'Username does not exist.'
