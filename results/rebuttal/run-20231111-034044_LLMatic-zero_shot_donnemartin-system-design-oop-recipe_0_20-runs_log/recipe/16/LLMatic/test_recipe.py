import pytest
from recipe import Recipe

def test_submit_recipe():
	recipe = Recipe('Pizza', ['Dough', 'Cheese', 'Tomato Sauce'], 'Bake at 350 for 20 minutes', ['pizza.jpg'], ['Italian'], {})
	mock_db = recipe.submit_recipe()
	assert 'Pizza' in mock_db


def test_edit_recipe():
	recipe = Recipe('Pizza', ['Dough', 'Cheese', 'Tomato Sauce'], 'Bake at 350 for 20 minutes', ['pizza.jpg'], ['Italian'], {})
	new_recipe = Recipe('Pizza', ['Dough', 'Cheese', 'Tomato Sauce', 'Pepperoni'], 'Bake at 350 for 20 minutes', ['pizza.jpg'], ['Italian'], {})
	recipe.edit_recipe(new_recipe)
	assert 'Pepperoni' in recipe.ingredients


def test_delete_recipe():
	recipe = Recipe('Pizza', ['Dough', 'Cheese', 'Tomato Sauce'], 'Bake at 350 for 20 minutes', ['pizza.jpg'], ['Italian'], {})
	mock_db = recipe.submit_recipe()
	recipe.delete_recipe(mock_db)
	assert 'Pizza' not in mock_db


def test_rate_recipe():
	recipe = Recipe('Pizza', ['Dough', 'Cheese', 'Tomato Sauce'], 'Bake at 350 for 20 minutes', ['pizza.jpg'], ['Italian'], {})
	recipe.rate_recipe('User1', 5)
	assert recipe.user_ratings['User1'] == [5]
