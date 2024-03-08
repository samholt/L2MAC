import pytest
from models import User
from auth import register_user, hash_password


def test_create_user():
	user = User.create('user3', hash_password('password3'), 'user3@example.com')
	assert user.username == 'user3'
	assert user.password == hash_password('password3')
	assert user.email == 'user3@example.com'


def test_user_exists():
	register_user('user1', 'password1', 'user1@example.com')
	assert User.exists('user1') == True
	register_user('user3', 'password3', 'user3@example.com')
	assert User.exists('user3') == True


def test_get_user():
	register_user('user1', 'password1', 'user1@example.com')
	user = User.get('user1')
	assert user.username == 'user1'
	assert user.password == hash_password('password1')
	assert user.email == 'user1@example.com'


def test_validate_password():
	register_user('user1', 'password1', 'user1@example.com')
	assert User.validate_password('user1', hash_password('password1')) == True
	assert User.validate_password('user1', hash_password('wrongpassword')) == False
