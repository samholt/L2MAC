import pytest
from recipe import Recipe

def test_recipe_creation():
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan', ['pancakes.jpg'], ['Breakfast', 'Easy'])
	assert recipe.name == 'Pancakes'
	assert recipe.ingredients == ['Flour', 'Eggs', 'Milk']
	assert recipe.instructions == 'Mix ingredients and cook on pan'
	assert recipe.images == ['pancakes.jpg']
	assert recipe.categories == ['Breakfast', 'Easy']

def test_recipe_edit():
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan', ['pancakes.jpg'], ['Breakfast', 'Easy'])
	recipe.edit_recipe(name='Waffles', ingredients=['Flour', 'Eggs', 'Milk', 'Baking Powder'], instructions='Mix ingredients and cook in waffle iron', images=['waffles.jpg'], categories=['Breakfast', 'Medium'])
	assert recipe.name == 'Waffles'
	assert recipe.ingredients == ['Flour', 'Eggs', 'Milk', 'Baking Powder']
	assert recipe.instructions == 'Mix ingredients and cook in waffle iron'
	assert recipe.images == ['waffles.jpg']
	assert recipe.categories == ['Breakfast', 'Medium']

def test_recipe_delete():
	recipe = Recipe('Pancakes', ['Flour', 'Eggs', 'Milk'], 'Mix ingredients and cook on pan', ['pancakes.jpg'], ['Breakfast', 'Easy'])
	recipe.delete_recipe()
	assert recipe.name == None
	assert recipe.ingredients == None
	assert recipe.instructions == None
	assert recipe.images == None
	assert recipe.categories == None
