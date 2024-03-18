import pytest
from user_accounts import UserAccounts


def test_create_account():
	user_accounts = UserAccounts()
	username = 'test_user'
	assert user_accounts.create_account(username) is None
	assert user_accounts.create_account(username) == None


def test_get_user_urls():
	user_accounts = UserAccounts()
	username = 'test_user'
	user_accounts.create_account(username)
	assert user_accounts.get_user_urls(username) == {}


def test_add_url_to_user():
	user_accounts = UserAccounts()
	username = 'test_user'
	user_accounts.create_account(username)
	assert user_accounts.add_url_to_user(username, 'https://www.google.com', 'abcdef')


def test_delete_url_from_user():
	user_accounts = UserAccounts()
	username = 'test_user'
	user_accounts.create_account(username)
	user_accounts.add_url_to_user(username, 'https://www.google.com', 'abcdef')
	assert user_accounts.delete_url_from_user(username, 'abcdef')


def test_get_user_analytics():
	user_accounts = UserAccounts()
	username = 'test_user'
	user_accounts.create_account(username)
	user_accounts.add_url_to_user(username, 'https://www.google.com', 'abcdef')
	assert user_accounts.get_user_analytics(username, None) == {'abcdef': None}

