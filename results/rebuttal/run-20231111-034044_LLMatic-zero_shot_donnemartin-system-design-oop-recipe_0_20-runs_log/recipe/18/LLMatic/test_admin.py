import pytest
from admin import Admin
from user import User
from recipe import Recipe


def test_admin_functions():
	admin = Admin()
	user = User('test_user', 'password')
	recipe = Recipe('test_recipe', ['ingredient1', 'ingredient2'], 'instructions', 'image.jpg', ['category1', 'category2'])

	admin.add_user(user)
	admin.add_recipe(recipe)
	assert admin.get_site_statistics() == {'Number of Users': 1, 'Number of Recipes': 1}

	admin.remove_user(user)
	admin.remove_recipe(recipe)
	assert admin.get_site_statistics() == {'Number of Users': 0, 'Number of Recipes': 0}

	admin.add_user(user)
	user.submit_recipe(recipe)
	assert admin.get_user_engagement() == {'test_user': 1}

	admin.remove_user(user)
	assert admin.get_user_engagement() == {}
