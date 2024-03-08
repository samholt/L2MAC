import pytest
from recipe import Recipe

def test_submit_recipe():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Cook pasta and add sauce', ['image1.jpg'], ['Italian'])
	assert recipe.submit_recipe() == recipe

def test_edit_recipe():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Cook pasta and add sauce', ['image1.jpg'], ['Italian'])
	edited_recipe = recipe.edit_recipe('Spaghetti', ['Spaghetti', 'Tomato Sauce'], 'Cook spaghetti and add sauce', ['image2.jpg'], ['Italian'])
	assert edited_recipe.name == 'Spaghetti'

def test_delete_recipe():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Cook pasta and add sauce', ['image1.jpg'], ['Italian'])
	assert recipe.delete_recipe() == {}

def test_rate_recipe():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Cook pasta and add sauce', ['image1.jpg'], ['Italian'])
	recipe.rate_recipe(5)
	assert recipe.rate_recipe(4) == 4.5
