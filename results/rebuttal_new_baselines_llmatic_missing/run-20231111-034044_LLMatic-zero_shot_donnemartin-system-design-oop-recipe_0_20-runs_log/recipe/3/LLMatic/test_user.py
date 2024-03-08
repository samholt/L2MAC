import pytest
from user import User


def test_create_account():
	user = User('test_user', 'test_password')
	response = user.create_account('new_user', 'new_password', ['Italian', 'Mexican'])
	assert response == {'message': 'Account created successfully', 'user': {'username': 'new_user', 'preferences': ['Italian', 'Mexican']}}


def test_manage_account():
	user = User('test_user', 'test_password')
	user.manage_account(username='new_user', password='new_password', preferences=['Italian', 'Mexican'])
	assert user.username == 'new_user'
	assert user.password == 'new_password'
	assert user.preferences == ['Italian', 'Mexican']


def test_save_favorite_recipe():
	user = User('test_user', 'test_password')
	user.save_favorite_recipe('Spaghetti')
	assert user.favorite_recipes == ['Spaghetti']


def test_follow_user():
	user1 = User('test_user1', 'test_password1')
	user2 = User('test_user2', 'test_password2')
	user1.follow_user(user2)
	assert user1.followed_users == [user2]
