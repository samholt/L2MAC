import pytest
from user import User

def test_create_user():
	user = User('1', 'Test User', 'test@example.com', 'password')
	assert user.id == '1'
	assert user.name == 'Test User'
	assert user.email == 'test@example.com'
	assert user.password == 'password'


def test_authenticate_user():
	user = User('1', 'Test User', 'test@example.com', 'password')
	assert user.authenticate_user('test@example.com', 'password') == True
	assert user.authenticate_user('wrong@example.com', 'password') == False
	assert user.authenticate_user('test@example.com', 'wrongpassword') == False


def test_update_user():
	user = User('1', 'Test User', 'test@example.com', 'password')
	user.update_user(name='Updated User', email='updated@example.com', password='newpassword')
	assert user.name == 'Updated User'
	assert user.email == 'updated@example.com'
	assert user.password == 'newpassword'
