import pytest
from admin import Admin
from recipe import Recipe

def test_admin_creation():
	admin = Admin('admin', 'password')
	assert admin.username == 'admin'
	assert admin.password == 'password'


def test_manage_recipe():
	admin = Admin('admin', 'password')
	recipe = Recipe('recipe1', 'description', 30, 'Easy')
	admin.manage_recipe(recipe)
	assert recipe in admin.managed_recipes


def test_remove_inappropriate_content():
	admin = Admin('admin', 'password')
	recipe = Recipe('recipe1', 'description', 30, 'Easy')
	admin.manage_recipe(recipe)
	admin.remove_inappropriate_content(recipe)
	assert recipe not in admin.managed_recipes
