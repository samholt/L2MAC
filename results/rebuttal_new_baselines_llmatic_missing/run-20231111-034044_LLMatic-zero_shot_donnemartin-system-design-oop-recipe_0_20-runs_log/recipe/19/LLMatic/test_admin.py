import pytest
from admin import Admin
from recipe import Recipe

def test_admin_creation():
	admin = Admin('admin', 'admin')
	assert admin.username == 'admin'
	assert admin.password == 'admin'


def test_manage_recipe():
	admin = Admin('admin', 'admin')
	recipe = Recipe('Pasta', 'Boil water, add pasta, cook for 10 minutes', ['image1', 'image2'], ['Italian', 'Pasta'], [])
	admin.manage_recipe(recipe)
	assert recipe in admin.managed_recipes


def test_remove_inappropriate_content():
	admin = Admin('admin', 'admin')
	recipe = Recipe('Pasta', 'Boil water, add pasta, cook for 10 minutes', ['image1', 'image2'], ['Italian', 'Pasta'], [])
	admin.manage_recipe(recipe)
	admin.remove_inappropriate_content(recipe)
	assert recipe not in admin.managed_recipes
