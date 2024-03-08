import pytest
from recipes import Recipe


def test_submit_recipe():
	recipe = Recipe()
	response = recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'})
	assert response == {'status': 'Recipe submitted successfully'}


def test_get_recipe():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'})
	response = recipe.get_recipe('1')
	assert response == {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'}


def test_edit_recipe():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'})
	response = recipe.edit_recipe('1', {'name': 'Spaghetti', 'ingredients': ['Spaghetti', 'Tomato Sauce'], 'instructions': 'Boil spaghetti, add sauce', 'category': 'Italian'})
	assert response == {'status': 'Recipe updated successfully'}


def test_delete_recipe():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'})
	response = recipe.delete_recipe('1')
	assert response == {'status': 'Recipe deleted successfully'}


def test_search_by_ingredients():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'})
	response = recipe.search_by_ingredients(['Pasta'])
	assert response == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'}]


def test_search_by_name():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'})
	response = recipe.search_by_name('Pasta')
	assert response == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'}]


def test_search_by_category():
	recipe = Recipe()
	recipe.submit_recipe('1', {'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'})
	response = recipe.search_by_category('Italian')
	assert response == [{'name': 'Pasta', 'ingredients': ['Pasta', 'Tomato Sauce'], 'instructions': 'Boil pasta, add sauce', 'category': 'Italian'}]
