import pytest
from user_accounts import User, UserAccounts


def test_user_creation():
	user = User('test', 'password')
	assert user.username == 'test'
	assert user.password == 'password'
	assert user.urls == {}


def test_user_add_url():
	user = User('test', 'password')
	user.add_url('http://example.com', 'exmpl')
	assert user.urls == {'exmpl': 'http://example.com'}


def test_user_get_url():
	user = User('test', 'password')
	user.add_url('http://example.com', 'exmpl')
	assert user.get_url('exmpl') == 'http://example.com'


def test_user_delete_url():
	user = User('test', 'password')
	user.add_url('http://example.com', 'exmpl')
	user.delete_url('exmpl')
	assert user.urls == {}


def test_user_update_url():
	user = User('test', 'password')
	user.add_url('http://example.com', 'exmpl')
	user.update_url('exmpl', 'http://newexample.com')
	assert user.urls == {'exmpl': 'http://newexample.com'}


def test_user_accounts_register():
	accounts = UserAccounts()
	assert accounts.register('test', 'password')
	assert not accounts.register('test', 'password')


def test_user_accounts_login():
	accounts = UserAccounts()
	accounts.register('test', 'password')
	assert accounts.login('test', 'password')
	assert not accounts.login('test', 'wrongpassword')
	assert not accounts.login('wronguser', 'password')


def test_user_accounts_get_user():
	accounts = UserAccounts()
	accounts.register('test', 'password')
	user = accounts.get_user('test')
	assert user.username == 'test'
	assert user.password == 'password'
