import pytest
from recipes import Recipe


def test_recipe_submission():
	recipe = Recipe()
	recipe_data = {'ingredients': 'eggs, milk, flour', 'instructions': 'Mix ingredients and bake', 'images': 'image.jpg', 'category': 'Dessert'}
	recipe.submit_recipe('1', recipe_data)
	assert recipe.get_recipe('1') == recipe_data


def test_recipe_edit():
	recipe = Recipe()
	recipe_data = {'ingredients': 'eggs, milk, flour', 'instructions': 'Mix ingredients and bake', 'images': 'image.jpg', 'category': 'Dessert'}
	recipe.submit_recipe('1', recipe_data)
	new_recipe_data = {'ingredients': 'eggs, milk, flour, sugar', 'instructions': 'Mix ingredients and bake', 'images': 'image.jpg', 'category': 'Dessert'}
	recipe.edit_recipe('1', new_recipe_data)
	assert recipe.get_recipe('1') == new_recipe_data


def test_recipe_delete():
	recipe = Recipe()
	recipe_data = {'ingredients': 'eggs, milk, flour', 'instructions': 'Mix ingredients and bake', 'images': 'image.jpg', 'category': 'Dessert'}
	recipe.submit_recipe('1', recipe_data)
	recipe.delete_recipe('1')
	assert recipe.get_recipe('1') is None
