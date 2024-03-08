import pytest
from admin import Admin
from user import User
from recipe import Recipe


def test_admin():
	admin = Admin()
	user = User('test_user', 'password', 'test_user@example.com')
	recipe = Recipe('test_recipe', ['ingredient1', 'ingredient2'], 'instructions', ['image1', 'image2'], ['category1', 'category2'])

	admin.add_user(user)
	admin.add_recipe(recipe)

	assert len(admin.users) == 1
	assert len(admin.recipes) == 1

	admin.remove_user('test_user')
	admin.remove_recipe('test_recipe')

	assert len(admin.users) == 0
	assert len(admin.recipes) == 0

	statistics = admin.get_site_statistics()
	assert statistics['number_of_users'] == 0
	assert statistics['number_of_recipes'] == 0
