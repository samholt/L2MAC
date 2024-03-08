import pytest
from recipe import Recipe, RecipeValidator

def test_recipe_creation():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta, add sauce', ['image1.jpg'], ['Italian'])
	assert recipe.name == 'Pasta'
	assert recipe.ingredients == ['Pasta', 'Tomato Sauce']
	assert recipe.instructions == 'Boil pasta, add sauce'
	assert recipe.images == ['image1.jpg']
	assert recipe.categories == ['Italian']


def test_recipe_edit():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta, add sauce', ['image1.jpg'], ['Italian'])
	recipe.edit_recipe('Pizza', ['Dough', 'Tomato Sauce', 'Cheese'], 'Bake dough, add sauce and cheese', ['image2.jpg'], ['Italian'])
	assert recipe.name == 'Pizza'
	assert recipe.ingredients == ['Dough', 'Tomato Sauce', 'Cheese']
	assert recipe.instructions == 'Bake dough, add sauce and cheese'
	assert recipe.images == ['image2.jpg']
	assert recipe.categories == ['Italian']


def test_recipe_delete():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta, add sauce', ['image1.jpg'], ['Italian'])
	recipe.delete_recipe()
	assert recipe.name == None
	assert recipe.ingredients == None
	assert recipe.instructions == None
	assert recipe.images == None
	assert recipe.categories == None


def test_recipe_validator():
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Boil pasta, add sauce', ['image1.jpg'], ['Italian'])
	assert RecipeValidator.validate(recipe) == True
	recipe = Recipe('', [], '', [], [])
	assert RecipeValidator.validate(recipe) == False
