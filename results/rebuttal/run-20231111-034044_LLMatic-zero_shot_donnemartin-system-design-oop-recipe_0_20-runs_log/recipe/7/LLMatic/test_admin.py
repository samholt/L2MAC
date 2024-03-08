import pytest
from admin import Admin


def test_manage_recipes():
	admin = Admin()
	admin.recipes = {'1': 'Recipe 1', '2': 'Recipe 2'}
	assert admin.manage_recipes('1', 'view') == 'Recipe 1'
	assert admin.manage_recipes('1', 'remove') == 'Recipe removed successfully'
	assert admin.manage_recipes('1', 'view') == 'Recipe not found'


def test_manage_users():
	admin = Admin()
	admin.users = {'1': 'User 1', '2': 'User 2'}
	assert admin.manage_users('1', 'view') == 'User 1'
	assert admin.manage_users('1', 'remove') == 'User removed successfully'
	assert admin.manage_users('1', 'view') == 'User not found'


def test_monitor_site_usage():
	admin = Admin()
	admin.site_usage = {'total_visits': 10, 'total_time_spent': 20, 'total_recipes_submitted': 30}
	assert admin.monitor_site_usage() == {'total_visits': 10, 'total_time_spent': 20, 'total_recipes_submitted': 30}
