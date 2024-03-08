import pytest
from auth import register_user, login_user, logout_user, hash_password
from models import User


def test_register_login_logout():
	User.users = {}
	assert register_user('testuser', 'password', 'testuser@example.com')
	assert login_user('testuser', 'password')
	assert logout_user('testuser')
	assert not login_user('testuser', 'wrongpassword')


def test_password_hashing():
	assert hash_password('password') == hash_password('password')
	assert hash_password('password') != hash_password('differentpassword')
