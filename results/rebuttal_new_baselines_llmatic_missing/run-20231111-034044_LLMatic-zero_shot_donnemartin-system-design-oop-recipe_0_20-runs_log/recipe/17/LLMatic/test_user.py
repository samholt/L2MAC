import pytest
from user import User

def test_user_creation():
	user = User('testuser', 'testpassword', 'testuser@test.com')
	assert user.username == 'testuser'
	assert user.password == 'testpassword'
	assert user.email == 'testuser@test.com'
	assert user.submitted_recipes == []
	assert user.favorite_recipes == []

def test_submit_recipe():
	user = User('testuser', 'testpassword', 'testuser@test.com')
	user.submit_recipe('recipe1')
	assert 'recipe1' in user.submitted_recipes

def test_favorite_recipe():
	user = User('testuser', 'testpassword', 'testuser@test.com')
	user.favorite_recipe('recipe1')
	assert 'recipe1' in user.favorite_recipes

def test_remove_favorite_recipe():
	user = User('testuser', 'testpassword', 'testuser@test.com')
	user.favorite_recipe('recipe1')
	user.remove_favorite_recipe('recipe1')
	assert 'recipe1' not in user.favorite_recipes
