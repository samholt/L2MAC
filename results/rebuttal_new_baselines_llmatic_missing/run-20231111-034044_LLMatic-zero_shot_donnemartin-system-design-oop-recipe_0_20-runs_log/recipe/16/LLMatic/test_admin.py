import pytest
from admin import Admin
from recipe import Recipe

def test_admin_class():
	admin = Admin('admin', 'admin')
	assert isinstance(admin, Admin)

	recipe = Recipe('test', [], '', [], [], {})
	admin.submit_recipe(recipe)
	assert recipe in admin.submitted_recipes

	admin.manage_recipes(recipe, 'delete')
	assert recipe not in admin.submitted_recipes

	# Test for edit and remove_inappropriate_content methods
	# will be added after their implementation
