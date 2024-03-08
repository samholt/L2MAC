import pytest
from user_accounts import UserAccount


def test_create_account():
	user_account = UserAccount()
	assert user_account.create_account('testuser') == 'Account created successfully.'
	assert user_account.create_account('testuser') == 'Username already exists.'


def test_view_urls():
	user_account = UserAccount()
	user_account.create_account('testuser')
	assert user_account.view_urls('testuser') == {}
	assert user_account.view_urls('nonexistentuser') == 'Username does not exist.'


def test_edit_url():
	user_account = UserAccount()
	user_account.create_account('testuser')
	user_account.accounts['testuser']['old_url'] = 'short_url'
	assert user_account.edit_url('testuser', 'old_url', 'new_url') == 'URL edited successfully.'
	assert user_account.edit_url('testuser', 'nonexistenturl', 'new_url') == 'URL does not exist.'
	assert user_account.edit_url('nonexistentuser', 'old_url', 'new_url') == 'Username does not exist.'


def test_delete_url():
	user_account = UserAccount()
	user_account.create_account('testuser')
	user_account.accounts['testuser']['url'] = 'short_url'
	assert user_account.delete_url('testuser', 'url') == 'URL deleted successfully.'
	assert user_account.delete_url('testuser', 'nonexistenturl') == 'URL does not exist.'
	assert user_account.delete_url('nonexistentuser', 'url') == 'Username does not exist.'
