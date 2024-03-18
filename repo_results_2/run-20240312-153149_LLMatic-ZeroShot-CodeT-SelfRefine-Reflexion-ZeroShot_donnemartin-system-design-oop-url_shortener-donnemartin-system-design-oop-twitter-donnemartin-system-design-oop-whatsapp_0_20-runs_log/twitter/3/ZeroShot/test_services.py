import pytest
from services import register_user, authenticate_user, get_user, update_user
from models import User


def test_register_user():
	data = {'username': 'test', 'email': 'test@test.com', 'password': 'test'}
	user = register_user(data)
	assert user.username == data['username']
	assert user.email == data['email']


def test_authenticate_user():
	data = {'username': 'test', 'password': 'test'}
	user = authenticate_user(data)
	assert user.username == data['username']


def test_get_user():
	username = 'test'
	user = get_user(username)
	assert user.username == username


def test_update_user():
	username = 'test'
	data = {'bio': 'This is a test bio'}
	user = update_user(username, data)
	assert user.bio == data['bio']
