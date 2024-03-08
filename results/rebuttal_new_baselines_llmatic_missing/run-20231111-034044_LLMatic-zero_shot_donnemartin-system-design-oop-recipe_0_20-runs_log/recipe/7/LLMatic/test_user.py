import pytest
from user import User

def test_create_account():
	user = User('test', 'password')
	user.create_account('new_test', 'new_password')
	assert user.username == 'new_test'
	assert user.password == 'new_password'

def test_manage_account():
	user = User('test', 'password')
	user.manage_account('new_test', 'new_password')
	assert user.username == 'new_test'
	assert user.password == 'new_password'

def test_save_favorite_recipe():
	user = User('test', 'password')
	user.save_favorite_recipe('recipe')
	assert 'recipe' in user.favorite_recipes
