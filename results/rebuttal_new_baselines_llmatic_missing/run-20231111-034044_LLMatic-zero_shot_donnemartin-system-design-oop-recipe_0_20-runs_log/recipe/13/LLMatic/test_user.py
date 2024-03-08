import pytest
from user import User, Profile


def test_user_creation():
	user = User('testuser', 'password', 'testuser@example.com')
	assert user.username == 'testuser'
	assert user.password == 'password'
	assert user.email == 'testuser@example.com'
	assert user.submitted_recipes == []
	assert user.favorite_recipes == []


def test_submit_recipe():
	user = User('testuser', 'password', 'testuser@example.com')
	user.submit_recipe('recipe1')
	assert user.submitted_recipes == ['recipe1']


def test_favorite_recipe():
	user = User('testuser', 'password', 'testuser@example.com')
	user.favorite_recipe('recipe1')
	assert user.favorite_recipes == ['recipe1']


def test_remove_favorite_recipe():
	user = User('testuser', 'password', 'testuser@example.com')
	user.favorite_recipe('recipe1')
	user.remove_favorite_recipe('recipe1')
	assert user.favorite_recipes == []


def test_profile_display():
	user = User('testuser', 'password', 'testuser@example.com')
	profile = Profile(user)
	user.submit_recipe('recipe1')
	user.favorite_recipe('recipe1')
	assert profile.display_submitted_recipes() == ['recipe1']
	assert profile.display_favorite_recipes() == ['recipe1']
