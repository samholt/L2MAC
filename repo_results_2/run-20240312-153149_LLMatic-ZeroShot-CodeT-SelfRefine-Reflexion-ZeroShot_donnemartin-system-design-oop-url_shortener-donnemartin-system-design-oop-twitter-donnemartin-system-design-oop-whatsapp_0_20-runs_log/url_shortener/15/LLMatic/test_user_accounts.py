import pytest
from user_accounts import UserAccounts


def test_create_account():
	user_accounts = UserAccounts()
	assert user_accounts.create_account('test') == 'Account created successfully.'
	assert user_accounts.create_account('test') == 'Username already exists.'


def test_view_urls():
	user_accounts = UserAccounts()
	user_accounts.create_account('test')
	assert user_accounts.view_urls('test') == {}
	assert user_accounts.view_urls('nonexistent') == 'Username does not exist.'


def test_edit_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('test')
	user_accounts.users['test']['url'] = {'clicks': 0}
	assert user_accounts.edit_url('test', 'url', 'new_url') == 'URL edited successfully.'
	assert 'url' not in user_accounts.users['test'].keys()
	assert 'new_url' in user_accounts.users['test'].keys()
	assert user_accounts.edit_url('test', 'url', 'new_url') == 'Invalid username or URL.'


def test_delete_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('test')
	user_accounts.users['test']['url'] = {'clicks': 0}
	assert user_accounts.delete_url('test', 'url') == 'URL deleted successfully.'
	assert user_accounts.delete_url('test', 'url') == 'Invalid username or URL.'


def test_view_analytics():
	user_accounts = UserAccounts()
	user_accounts.create_account('test')
	user_accounts.users['test']['url'] = {'clicks': 0}
	assert user_accounts.view_analytics('test') == {'url': 0}
	assert user_accounts.view_analytics('nonexistent') == 'Username does not exist.'
