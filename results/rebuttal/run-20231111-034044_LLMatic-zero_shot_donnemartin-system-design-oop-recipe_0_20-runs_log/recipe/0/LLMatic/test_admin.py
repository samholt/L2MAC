import pytest
from admin import Admin
from recipe import Recipe
from review import Review


def test_admin():
	admin = Admin('Admin', 'admin@example.com')
	recipe = Recipe('1', 'Pasta', 'Italian', ['pasta', 'tomato', 'basil'], 'Boil pasta, add sauce', {}, {})
	review = Review('1', 'User', 2, 'This is a bad recipe')

	admin.add_recipe(recipe)
	assert len(admin.manage_recipes()) == 1

	admin.remove_recipe('1')
	assert len(admin.manage_recipes()) == 0

	admin.add_recipe(recipe)
	admin.remove_inappropriate_content(review)
	assert review.content == 'This review has been removed due to inappropriate content.'
