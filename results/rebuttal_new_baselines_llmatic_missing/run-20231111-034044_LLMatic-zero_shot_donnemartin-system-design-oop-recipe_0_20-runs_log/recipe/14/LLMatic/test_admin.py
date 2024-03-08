import pytest
from admin import Admin


def test_manage_recipes():
	admin = Admin()
	admin.database = {'1': 'Recipe 1', '2': 'Recipe 2'}

	assert admin.manage_recipes('1', 'view') == 'Recipe 1'
	assert admin.manage_recipes('3', 'view') == 'Recipe not found'
	assert admin.manage_recipes('1', 'delete') == 'Recipe deleted'
	assert admin.manage_recipes('1', 'view') == 'Recipe not found'


def test_remove_inappropriate_content():
	admin = Admin()
	admin.database = {'1': 'Content 1', '2': 'Content 2'}

	assert admin.remove_inappropriate_content('1') == 'Content removed'
	assert admin.remove_inappropriate_content('3') == 'Content not found'
