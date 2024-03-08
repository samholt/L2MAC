import pytest
from admin import Admin

def test_admin():
	admin = Admin()

	# Test manage_recipes
	assert admin.manage_recipes('recipe1', 'view') == 'Recipe not found'
	admin.recipes['recipe1'] = 'Recipe 1'
	assert admin.manage_recipes('recipe1', 'view') == 'Recipe 1'
	assert admin.manage_recipes('recipe1', 'remove') == 'Recipe removed'
	assert admin.manage_recipes('recipe1', 'view') == 'Recipe not found'

	# Test manage_users
	assert admin.manage_users('user1', 'view') == 'User not found'
	admin.users['user1'] = 'User 1'
	assert admin.manage_users('user1', 'view') == 'User 1'
	assert admin.manage_users('user1', 'remove') == 'User removed'
	assert admin.manage_users('user1', 'view') == 'User not found'

	# Test monitor_site_usage
	assert admin.monitor_site_usage() == {'total_visits': 0, 'total_recipes': 0, 'total_users': 0}
