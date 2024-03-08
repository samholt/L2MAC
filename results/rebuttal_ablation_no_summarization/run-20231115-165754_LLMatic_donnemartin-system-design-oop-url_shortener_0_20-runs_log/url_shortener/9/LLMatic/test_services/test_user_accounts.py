import pytest
from services.user_accounts import UserAccounts


def test_create_account():
	user_accounts = UserAccounts()
	assert user_accounts.create_account('testuser') == 'Account created successfully'
	assert user_accounts.create_account('testuser') == 'Username already exists'


def test_add_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('testuser')
	assert user_accounts.add_url('testuser', 'short', 'original') == 'URL added successfully'
	assert user_accounts.add_url('nonexistent', 'short', 'original') == 'Username does not exist'


def test_view_urls():
	user_accounts = UserAccounts()
	user_accounts.create_account('testuser')
	user_accounts.add_url('testuser', 'short', 'original')
	assert user_accounts.view_urls('testuser') == {'short': 'original'}
	assert user_accounts.view_urls('nonexistent') == 'Username does not exist'


def test_edit_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('testuser')
	user_accounts.add_url('testuser', 'short', 'original')
	assert user_accounts.edit_url('testuser', 'short', 'new') == 'URL edited successfully'
	assert user_accounts.edit_url('testuser', 'nonexistent', 'new') == 'URL does not exist'


def test_delete_url():
	user_accounts = UserAccounts()
	user_accounts.create_account('testuser')
	user_accounts.add_url('testuser', 'short', 'original')
	assert user_accounts.delete_url('testuser', 'short') == 'URL deleted successfully'
	assert user_accounts.delete_url('testuser', 'nonexistent') == 'URL does not exist'
