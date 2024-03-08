import pytest
from user import User


def test_create_account():
	user = User('test_user', 'test_password')
	assert user.username == 'test_user'
	assert user.password == 'test_password'


def test_manage_account():
	user = User('test_user', 'test_password')
	user.manage_account('new_user', 'new_password')
	assert user.username == 'new_user'
	assert user.password == 'new_password'


def test_save_favorite_recipe():
	user = User('test_user', 'test_password')
	recipe = {'name': 'Pizza', 'cuisine': 'Italian'}
	user.save_favorite_recipe(recipe)
	assert user.favorite_recipes[0] == recipe


def test_set_preferences():
	user = User('test_user', 'test_password')
	user.set_preferences(['Italian', 'Mexican'])
	assert user.preferences == ['Italian', 'Mexican']


def test_set_interest_areas():
	user = User('test_user', 'test_password')
	user.set_interest_areas(['Italian', 'Mexican'])
	assert user.interest_areas == ['Italian', 'Mexican']
