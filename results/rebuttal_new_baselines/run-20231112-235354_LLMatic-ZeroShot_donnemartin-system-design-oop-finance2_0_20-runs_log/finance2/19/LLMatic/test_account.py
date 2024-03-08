import pytest
from account import User

def test_create_user():
	user = User('test_user', 'test_password')
	assert user.create_user() == {'username': 'test_user', 'password': 'test_password'}

def test_link_bank_account():
	user = User('test_user', 'test_password')
	assert user.link_bank_account() == True

def test_enable_multi_factor_auth():
	user = User('test_user', 'test_password')
	assert user.enable_multi_factor_auth() == True
