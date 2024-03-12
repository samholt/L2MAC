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

def test_edit_url():
	user_account = UserAccount()
	user_account.create_account('test', 'password')
	user_account.accounts['test']['urls'].append('http://example.com')
	assert user_account.edit_url('test', 'http://example.com', 'http://newexample.com') == 'URL edited successfully.'
	assert user_account.edit_url('test', 'http://nonexistent.com', 'http://newexample.com') == 'URL does not exist.'
	assert user_account.edit_url('nonexistent', 'http://example.com', 'http://newexample.com') == 'Username does not exist.'

def test_delete_url():
	user_account = UserAccount()
	user_account.create_account('test', 'password')
	user_account.accounts['test']['urls'].append('http://example.com')
	assert user_account.delete_url('test', 'http://example.com') == 'URL deleted successfully.'
	assert user_account.delete_url('test', 'http://nonexistent.com') == 'URL does not exist.'
	assert user_account.delete_url('nonexistent', 'http://example.com') == 'Username does not exist.'
