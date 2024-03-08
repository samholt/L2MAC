import pytest
from category import Category
from recipe import Recipe

def test_category():
	category = Category('Dessert')
	assert category.name == 'Dessert'
	assert category.recipes == []

	recipe = Recipe('Cake', 'Bake a cake', '30 mins', 'Easy')
	category.add_recipe(recipe)
	assert category.recipes == [recipe]

	search_result = category.search_recipes('Cake')
	assert search_result == [recipe]

	search_result = category.search_recipes('Pie')
	assert search_result == []
