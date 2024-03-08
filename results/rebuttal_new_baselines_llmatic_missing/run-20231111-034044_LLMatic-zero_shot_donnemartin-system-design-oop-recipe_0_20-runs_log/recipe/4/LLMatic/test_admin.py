import pytest
from admin import Admin


def test_manage_recipes():
	admin = Admin()
	admin.recipes = {1: 'Recipe 1', 2: 'Recipe 2'}

	assert admin.manage_recipes(1, 'view') == 'Recipe 1'
	assert admin.manage_recipes(1, 'delete') == 'Recipe deleted'
	assert admin.manage_recipes(1, 'view') == 'Recipe not found'


def test_remove_inappropriate_content():
	admin = Admin()
	admin.users = {1: {'content': [{'inappropriate': True, 'text': 'Bad content'}, {'inappropriate': False, 'text': 'Good content'}]}}

	assert admin.remove_inappropriate_content(1) == 'Inappropriate content removed'
	assert admin.users[1]['content'] == [{'inappropriate': False, 'text': 'Good content'}]
