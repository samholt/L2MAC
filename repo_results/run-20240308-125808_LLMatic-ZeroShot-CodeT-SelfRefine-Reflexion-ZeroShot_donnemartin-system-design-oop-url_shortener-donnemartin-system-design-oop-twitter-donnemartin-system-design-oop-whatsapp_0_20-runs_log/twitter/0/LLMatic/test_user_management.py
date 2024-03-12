import pytest
from user_management import User, UserManagement


def test_user_registration():
	um = UserManagement()
	um.register('email1', 'user1', 'password1')
	um.register('email2', 'user2', 'password2')
	assert len(um.users) == 2


def test_user_login():
	um = UserManagement()
	um.register('email1', 'user1', 'password1')
	um.register('email2', 'user2', 'password2')
	assert um.login('email1', 'password1') is not None
	assert um.login('email2', 'wrong_password') is None


def test_search_users_by_username():
	um = UserManagement()
	um.register('email1', 'user1', 'password1')
	um.register('email2', 'user2', 'password2')
	assert um.search_users_by_username('user1') is not None
	assert um.search_users_by_username('user3') is None
