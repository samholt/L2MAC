import pytest
from admin import Admin

admin = Admin()


def test_manage_recipes():
	admin.database['recipes'] = {'1': 'Recipe 1', '2': 'Recipe 2'}
	assert admin.manage_recipes('1', 'view') == 'Recipe 1'
	assert admin.manage_recipes('1', 'delete') == 'Recipe deleted successfully'
	assert admin.manage_recipes('1', 'view') == 'Recipe not found'


def test_remove_inappropriate_content():
	admin.database['content'] = {'1': 'Content 1', '2': 'Content 2'}
	assert admin.remove_inappropriate_content('1') == 'Content removed successfully'
	assert admin.remove_inappropriate_content('1') == 'Content not found'


def test_monitor_site_usage():
	admin.database['users'] = {'user1': {}, 'user2': {}}
	admin.database['recipes'] = {'1': 'Recipe 1', '2': 'Recipe 2'}
	assert admin.monitor_site_usage() == (2, 2)


def test_monitor_user_engagement():
	admin.database['users'] = {'user1': {'followed': ['user2']}, 'user2': {'followed': []}}
	assert admin.monitor_user_engagement() == {'user1': 1, 'user2': 0}
