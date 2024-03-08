import pytest
from services import create_user, create_recipe, add_favorite, users, recipes
from models import User, Recipe

def test_create_user():
	user = create_user(1, 'Test User')
	assert user == User(1, 'Test User')
	assert users[1] == user

def test_create_recipe():
	recipe = create_recipe(1, 'Test Recipe', ['ingredient1', 'ingredient2'], ['instruction1', 'instruction2'], 'image.jpg', ['category1', 'category2'])
	assert recipe == Recipe(1, 'Test Recipe', ['ingredient1', 'ingredient2'], ['instruction1', 'instruction2'], 'image.jpg', ['category1', 'category2'])
	assert recipes[1] == recipe

def test_add_favorite():
	user = create_user(2, 'Test User 2')
	recipe = create_recipe(2, 'Test Recipe 2', ['ingredient1', 'ingredient2'], ['instruction1', 'instruction2'], 'image.jpg', ['category1', 'category2'])
	add_favorite(2, 2)
	assert user.favorites == [2]
