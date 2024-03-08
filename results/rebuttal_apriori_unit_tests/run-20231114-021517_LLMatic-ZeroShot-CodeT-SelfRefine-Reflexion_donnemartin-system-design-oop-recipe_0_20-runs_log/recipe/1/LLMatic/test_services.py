import pytest
from services import *

# Existing tests...

def test_admin_manage_recipes():
	create_user('admin1', 'pass123', is_admin=True)
	submit_recipe(users_db['admin1'], 'Pizza', ['ingredient1', 'ingredient2'], 'Mix and cook', 'image_url', ['Italian'])
	manage_recipe('admin1', 'Pizza', {'title': 'Updated Pizza'})
	assert 'Updated Pizza' in recipes_db


def test_admin_remove_content():
	create_user('admin2', 'pass123', is_admin=True)
	submit_recipe(users_db['admin2'], 'Burger', ['ingredient1', 'ingredient2'], 'Mix and cook', 'image_url', ['American'])
	remove_recipe('admin2', 'Burger')
	assert 'Burger' not in recipes_db


def test_admin_monitoring():
	create_user('admin3', 'pass123', is_admin=True)
	submit_recipe(users_db['admin3'], 'Pasta', ['ingredient1', 'ingredient2'], 'Mix and cook', 'image_url', ['Italian'])
	stats = get_site_statistics('admin3')
	assert stats['total_users'] == 3
	assert stats['total_recipes'] == 2
