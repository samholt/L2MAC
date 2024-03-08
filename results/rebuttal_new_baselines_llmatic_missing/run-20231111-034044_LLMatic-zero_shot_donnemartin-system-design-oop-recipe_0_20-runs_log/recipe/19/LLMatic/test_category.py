import pytest
from category import Category
from recipe import Recipe

def test_category():
	category = Category('Dessert')
	assert category.name == 'Dessert'
	assert category.recipes == []

	recipe = Recipe('Cake', 'Bake a cake', '30 mins', 'Easy', [])
	category.add_recipe(recipe)
	assert recipe in category.recipes

	category.remove_recipe(recipe)
	assert recipe not in category.recipes
