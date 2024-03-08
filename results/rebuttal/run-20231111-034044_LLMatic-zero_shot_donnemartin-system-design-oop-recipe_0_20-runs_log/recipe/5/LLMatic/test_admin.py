import pytest
from admin import Admin
from user import User
from recipe import Recipe


def test_admin_manage_recipe():
	admin = Admin('admin', 'admin')
	user = User('user', 'user')
	recipe = Recipe('recipe', 'ingredients', 'instructions', 'images', 'category')
	user.submit_recipe(recipe)
	assert admin.manage_recipe(recipe) == 'Recipe managed successfully'
	assert admin.managed_recipes[recipe.name] == recipe


def test_admin_remove_recipe():
	admin = Admin('admin', 'admin')
	recipe = Recipe('recipe', 'ingredients', 'instructions', 'images', 'category')
	admin.managed_recipes[recipe.name] = recipe
	assert admin.remove_recipe(recipe) == 'Recipe removed successfully'
	assert recipe.name not in admin.managed_recipes


def test_admin_monitor_site_usage():
	admin = Admin('admin', 'admin')
	user1 = User('user1', 'user1')
	user2 = User('user2', 'user2')
	admin.follow_user(user1)
	admin.follow_user(user2)
	assert admin.monitor_site_usage() == {'total_users': 2, 'total_recipes': 0}


def test_admin_monitor_user_engagement():
	admin = Admin('admin', 'admin')
	user1 = User('user1', 'user1')
	user2 = User('user2', 'user2')
	recipe1 = Recipe('recipe1', 'ingredients', 'instructions', 'images', 'category')
	recipe2 = Recipe('recipe2', 'ingredients', 'instructions', 'images', 'category')
	user1.submit_recipe(recipe1)
	user2.submit_recipe(recipe2)
	admin.follow_user(user1)
	admin.follow_user(user2)
	assert admin.monitor_user_engagement() == {'average_submitted_recipes': 1.0}
