import pytest
from user import User

def test_user_creation():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'


def test_account_management():
	user = User('test_user', 'test_password')
	user.manage_account('new_user', 'new_password')
	assert user.username == 'new_user'
	assert user.password == 'new_password'


def test_save_favorite_recipe():
	user = User('test_user', 'test_password')
	user.save_favorite_recipe('test_recipe')
	assert 'test_recipe' in user.favorite_recipes


def test_follow_user():
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')
	user1.follow_user(user2)
	assert user2 in user1.following
	assert user2.submitted_recipes == user1.feed


def test_set_preferences():
	user = User('test_user', 'test_password')
	user.set_preferences(['vegan', 'gluten-free'])
	assert 'vegan' in user.preferences
	assert 'gluten-free' in user.preferences


def test_generate_recommendations():
	user = User('test_user', 'test_password')
	recommendations = user.generate_recommendations()
	assert 'recipe1' in recommendations
	assert 'recipe2' in recommendations
	assert 'recipe3' in recommendations


def test_receive_notification():
	user = User('test_user', 'test_password')
	user.receive_notification('New recipe available')
	assert 'New recipe available' in user.notifications
