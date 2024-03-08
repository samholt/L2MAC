import pytest
from admin import Admin
from recipe import Recipe


def test_manage_recipe():
	admin = Admin()
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Cook pasta and add sauce', ['image1.jpg'], ['Italian'])
	admin.manage_recipe(recipe)
	assert recipe in admin.get_managed_recipes()


def test_remove_recipe():
	admin = Admin()
	recipe = Recipe('Pasta', ['Pasta', 'Tomato Sauce'], 'Cook pasta and add sauce', ['image1.jpg'], ['Italian'])
	admin.manage_recipe(recipe)
	admin.remove_recipe(recipe)
	assert recipe not in admin.get_managed_recipes()
	assert recipe.name is None
