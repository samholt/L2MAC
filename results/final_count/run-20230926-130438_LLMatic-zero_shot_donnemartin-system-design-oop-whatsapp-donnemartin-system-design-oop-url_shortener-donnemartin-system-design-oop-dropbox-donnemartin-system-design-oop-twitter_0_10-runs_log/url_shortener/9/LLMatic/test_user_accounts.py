import pytest
from user_accounts import UserAccounts


def test_create_account():
	user_accounts = UserAccounts()
	assert user_accounts.create_account('test', 'test') == 'Account created successfully.'
	assert user_accounts.create_account('test', 'test') == 'Username already exists.'


def test_view_urls():
	user_accounts = UserAccounts()
	user_accounts.create_account('test', 'test')
	assert user_accounts.view_urls('test', 'test') == []
	assert user_accounts.view_urls('test', 'wrong') == 'Invalid credentials.'
	assert user_accounts.view_urls('wrong', 'test') == 'Invalid credentials.'


def test_edit_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('test', 'test')
	user_accounts.users['test']['urls'].append('old_url')
	assert user_accounts.edit_url('test', 'test', 'old_url', 'new_url') == 'URL edited successfully.'
	assert user_accounts.edit_url('test', 'test', 'old_url', 'new_url') == 'URL not found.'
	assert user_accounts.edit_url('test', 'wrong', 'old_url', 'new_url') == 'Invalid credentials.'
	assert user_accounts.edit_url('wrong', 'test', 'old_url', 'new_url') == 'Invalid credentials.'


def test_delete_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('test', 'test')
	user_accounts.users['test']['urls'].append('url')
	assert user_accounts.delete_url('test', 'test', 'url') == 'URL deleted successfully.'
	assert user_accounts.delete_url('test', 'test', 'url') == 'URL not found.'
	assert user_accounts.delete_url('test', 'wrong', 'url') == 'Invalid credentials.'
	assert user_accounts.delete_url('wrong', 'test', 'url') == 'Invalid credentials.'


def test_view_analytics():
	user_accounts = UserAccounts()
	user_accounts.create_account('test', 'test')
	assert user_accounts.view_analytics('test', 'test') == []
	assert user_accounts.view_analytics('test', 'wrong') == 'Invalid credentials.'
	assert user_accounts.view_analytics('wrong', 'test') == 'Invalid credentials.'
