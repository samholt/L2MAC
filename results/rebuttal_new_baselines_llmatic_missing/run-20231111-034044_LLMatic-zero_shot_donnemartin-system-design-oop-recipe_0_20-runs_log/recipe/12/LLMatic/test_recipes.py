import pytest
from recipes import Recipe


def test_recipe_submission():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Cook pasta. Add sauce.', 'images': [], 'category': 'Italian'})
	assert recipe.get_recipe('1') == {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Cook pasta. Add sauce.', 'images': [], 'category': 'Italian'}


def test_recipe_editing():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Cook pasta. Add sauce.', 'images': [], 'category': 'Italian'})
	recipe.edit_recipe('1', {'name': 'Spaghetti', 'ingredients': ['Spaghetti', 'Tomato Sauce'], 'instructions': 'Cook spaghetti. Add sauce.', 'images': [], 'category': 'Italian'})
	assert recipe.get_recipe('1') == {'name': 'Spaghetti', 'ingredients': ['Spaghetti', 'Tomato Sauce'], 'instructions': 'Cook spaghetti. Add sauce.', 'images': [], 'category': 'Italian'}


def test_recipe_deletion():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Cook pasta. Add sauce.', 'images': [], 'category': 'Italian'})
	recipe.delete_recipe('1')
	assert recipe.get_recipe('1') == None
