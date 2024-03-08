import pytest
from user_accounts import UserAccount

def test_create_account():
	user_account = UserAccount()
	assert user_account.create_account('testuser') == 'Account created successfully.'
	assert user_account.create_account('testuser') == 'Username already exists.'

def test_view_urls():
	user_account = UserAccount()
	user_account.create_account('testuser')
	assert user_account.view_urls('testuser') == []
	assert user_account.view_urls('nonexistentuser') == 'Username does not exist.'

def test_edit_url():
	user_account = UserAccount()
	user_account.create_account('testuser')
	assert user_account.edit_url('testuser', 'oldurl', 'newurl') == 'URL does not exist.'
	assert user_account.edit_url('nonexistentuser', 'oldurl', 'newurl') == 'Username does not exist.'

def test_delete_url():
	user_account = UserAccount()
	user_account.create_account('testuser')
	assert user_account.delete_url('testuser', 'url') == 'URL does not exist.'
	assert user_account.delete_url('nonexistentuser', 'url') == 'Username does not exist.'

def test_view_analytics():
	user_account = UserAccount()
	user_account.create_account('testuser')
	assert user_account.view_analytics('testuser') == 'Analytics for user: testuser'
	assert user_account.view_analytics('nonexistentuser') == 'Username does not exist.'
