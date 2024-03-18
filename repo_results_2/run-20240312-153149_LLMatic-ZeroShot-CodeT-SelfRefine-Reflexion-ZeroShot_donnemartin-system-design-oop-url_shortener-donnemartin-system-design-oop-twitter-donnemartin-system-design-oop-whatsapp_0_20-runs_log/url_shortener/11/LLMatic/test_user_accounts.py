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
	assert user_account.edit_url('test', 'old_url', 'new_url') == 'URL does not exist.'
	user_account.accounts['test']['urls'].append('old_url')
	assert user_account.edit_url('test', 'old_url', 'new_url') == 'URL edited successfully.'
	assert 'new_url' in user_account.accounts['test']['urls']

def test_delete_url():
	user_account = UserAccount()
	user_account.create_account('test', 'password')
	assert user_account.delete_url('test', 'url') == 'URL does not exist.'
	user_account.accounts['test']['urls'].append('url')
	assert user_account.delete_url('test', 'url') == 'URL deleted successfully.'
	assert 'url' not in user_account.accounts['test']['urls']

def test_view_analytics():
	user_account = UserAccount()
	user_account.create_account('test', 'password')
	assert user_account.view_analytics('test') == []
	assert user_account.view_analytics('nonexistent') == 'Username does not exist.'
