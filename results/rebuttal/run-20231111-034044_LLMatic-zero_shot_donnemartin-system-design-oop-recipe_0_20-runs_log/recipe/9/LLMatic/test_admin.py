import pytest
from admin import Admin


def test_manage_recipes():
	admin = Admin()
	admin.recipes = {'1': 'Recipe 1', '2': 'Recipe 2'}

	assert admin.manage_recipes('1', 'view') == 'Recipe 1'
	assert admin.manage_recipes('1', 'delete') == 'Recipe deleted successfully'
	assert admin.manage_recipes('1', 'view') == 'Recipe not found'


def test_manage_reviews():
	admin = Admin()
	admin.reviews = {'1': 'Review 1', '2': 'Review 2'}

	assert admin.manage_reviews('1', 'view') == 'Review 1'
	assert admin.manage_reviews('1', 'delete') == 'Review deleted successfully'
	assert admin.manage_reviews('1', 'view') == 'Review not found'
