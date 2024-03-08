import pytest
from recipe import Recipe

def test_recipe_creation():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta and add sauce', ['image1.jpg'], 'Italian', 'Main', 'Italian', 'Vegetarian')
	assert recipe.name == 'Pasta'
	assert recipe.ingredients == ['Pasta', 'Tomato Sauce']
	assert recipe.instructions == 'Boil pasta and add sauce'
	assert recipe.images == ['image1.jpg']
	assert recipe.category == 'Italian'
	assert recipe.type == 'Main'
	assert recipe.cuisine == 'Italian'
	assert recipe.diet == 'Vegetarian'

def test_submit_recipe():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta and add sauce', ['image1.jpg'], 'Italian', 'Main', 'Italian', 'Vegetarian')
	assert recipe.submit_recipe() == 'Recipe submitted successfully'

def test_edit_recipe():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta and add sauce', ['image1.jpg'], 'Italian', 'Main', 'Italian', 'Vegetarian')
	recipe.edit_recipe('Spaghetti', ['Spaghetti', 'Tomato Sauce'], 'Boil spaghetti and add sauce', ['image2.jpg'], 'Italian', 'Main', 'Italian', 'Vegetarian')
	assert recipe.name == 'Spaghetti'
	assert recipe.ingredients == ['Spaghetti', 'Tomato Sauce']
	assert recipe.instructions == 'Boil spaghetti and add sauce'
	assert recipe.images == ['image2.jpg']
	assert recipe.category == 'Italian'
	assert recipe.type == 'Main'
	assert recipe.cuisine == 'Italian'
	assert recipe.diet == 'Vegetarian'

def test_delete_recipe():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta and add sauce', ['image1.jpg'], 'Italian', 'Main', 'Italian', 'Vegetarian')
	recipe.submit_recipe()
	assert recipe.delete_recipe() == 'Recipe deleted successfully'

def test_validate_recipe_format():
	recipe = Recipe('', ['Pasta', 'Tomato Sauce'], 'Boil pasta and add sauce', ['image1.jpg'], 'Italian', 'Main', 'Italian', 'Vegetarian')
	assert recipe.validate_recipe_format() == False
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta and add sauce', ['image1.jpg'], 'Italian', 'Main', 'Italian', 'Vegetarian')
	assert recipe.validate_recipe_format() == True
