import pytest
from models.user import User

def test_create_user():
	user = User.create_user('John Doe', 'john@example.com', 'password')
	assert user.name == 'John Doe'
	assert user.email == 'john@example.com'
	assert user.password is not None


def test_authenticate_user():
	user = User.create_user('John Doe', 'john@example.com', 'password')
	assert user.authenticate_user('john@example.com', 'password') is True
	assert user.authenticate_user('john@example.com', 'wrongpassword') is False


def test_link_bank_account():
	user = User.create_user('John Doe', 'john@example.com', 'password')
	user.link_bank_account('Bank Account 1')
	assert 'Bank Account 1' in user.bank_accounts
