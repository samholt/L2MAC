import pytest
from category import Category
from recipe import Recipe
from user import User

def test_category():
	category = Category('Dessert')
	assert category.name == 'Dessert'
	assert category.recipes == []

	user = User('John', 'john@example.com')
	recipe = Recipe('Cake', 'Bake a cake', '30 mins', 'Easy', [], {})
	category.add_recipe(recipe)
	assert category.recipes == [recipe]

	category.remove_recipe(recipe)
	assert category.recipes == []
