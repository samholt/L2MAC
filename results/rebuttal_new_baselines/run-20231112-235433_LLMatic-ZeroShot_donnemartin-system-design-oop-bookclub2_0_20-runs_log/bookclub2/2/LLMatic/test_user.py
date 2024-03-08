import pytest
from user import User

def test_create_user():
	user = User.create_user('1', 'Test User', 'test@example.com', 'password')
	assert user.id == '1'
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
	assert user.password == 'password'

def test_authenticate():
	user = User.create_user('1', 'Test User', 'test@example.com', 'password')
	assert user.authenticate('test@example.com', 'password')
	assert not user.authenticate('wrong@example.com', 'password')
	assert not user.authenticate('test@example.com', 'wrongpassword')

def test_get_info():
	user = User.create_user('1', 'Test User', 'test@example.com', 'password')
	info = user.get_info()
	assert info['id'] == '1'
	assert info['name'] == 'Test User'
	assert info['email'] == 'test@example.com'
