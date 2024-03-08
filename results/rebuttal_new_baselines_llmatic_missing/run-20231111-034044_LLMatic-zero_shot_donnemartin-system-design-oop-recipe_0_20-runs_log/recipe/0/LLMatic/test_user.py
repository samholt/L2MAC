import pytest
from user import User

def test_user_creation():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'
	assert user.submitted_recipes == []
	assert user.favorite_recipes == []
	assert user.followed_users == []

def test_account_management():
	user = User('test_user', 'test_password')
	user.manage_account('new_user', 'new_password')
	assert user.username == 'new_user'
	assert user.password == 'new_password'

def test_save_favorite_recipe():
	user = User('test_user', 'test_password')
	user.save_favorite_recipe('recipe1')
	assert 'recipe1' in user.favorite_recipes

def test_follow_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user1.follow_user(user2)
	assert user2 in user1.followed_users
