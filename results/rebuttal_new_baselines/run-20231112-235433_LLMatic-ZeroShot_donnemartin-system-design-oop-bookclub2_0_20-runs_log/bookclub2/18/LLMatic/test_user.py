import pytest
from user import User

def test_create_user():
	user = User('test_user', 'test_password', 'test_email')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.email == 'test_email'
	assert user.book_clubs == []

def test_authenticate_user():
	user = User('test_user', 'test_password', 'test_email')
	assert user.authenticate_user('test_user', 'test_password')
	assert not user.authenticate_user('wrong_user', 'test_password')
	assert not user.authenticate_user('test_user', 'wrong_password')

def test_join_book_club():
	user = User('test_user', 'test_password', 'test_email')
	user.join_book_club('test_club')
	assert 'test_club' in user.book_clubs
