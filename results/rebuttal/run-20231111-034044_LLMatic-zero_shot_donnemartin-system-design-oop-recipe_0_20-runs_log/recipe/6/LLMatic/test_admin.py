import pytest
from admin import Admin

def test_admin():
	admin = Admin('admin', 'admin')

	# Test manage_recipes
	assert admin.manage_recipes('recipe1', 'add') == {'recipe1': 'Added'}
	assert admin.manage_recipes('recipe1', 'remove') == {}

	# Test remove_inappropriate_content
	admin.manage_recipes('recipe2', 'add')
	assert admin.remove_inappropriate_content('recipe2') == {}

	# Test monitor_site_usage
	assert admin.monitor_site_usage('user1', 'view') == {'user1': {'views': 1, 'actions': 0}}
	assert admin.monitor_site_usage('user1', 'action') == {'user1': {'views': 1, 'actions': 1}}

	# Test monitor_user_engagement
	assert admin.monitor_user_engagement('user1', 1) == {'user1': 1}
	assert admin.monitor_user_engagement('user1', 2) == {'user1': 3}
