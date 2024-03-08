import admin
import pytest

def test_manage_recipes():
	admin.db.recipes = {'1': 'Recipe 1', '2': 'Recipe 2'}
	assert admin.manage_recipes() == {'1': 'Recipe 1', '2': 'Recipe 2'}

def test_remove_content():
	admin.db.recipes = {'1': 'Recipe 1', '2': 'Recipe 2'}
	admin.remove_content('1')
	assert admin.manage_recipes() == {'2': 'Recipe 2'}
