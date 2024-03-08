import pytest
from user import User

def test_create_account():
	user = User('test', 'password')
	assert user.username == 'test'
	assert user.password == 'password'


def test_link_bank_account():
	user = User('test', 'password')
	user.link_bank_account('12345678')
	assert '12345678' in user.bank_accounts


def test_enable_mfa():
	user = User('test', 'password')
	user.enable_mfa()
	assert user.mfa_enabled == True


def test_disable_mfa():
	user = User('test', 'password')
	user.disable_mfa()
	assert user.mfa_enabled == False
