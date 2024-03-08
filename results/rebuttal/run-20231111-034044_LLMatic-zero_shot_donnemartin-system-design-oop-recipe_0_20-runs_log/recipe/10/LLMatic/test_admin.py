import pytest
from admin import Admin


def test_manage_recipe():
	admin = Admin('admin')
	assert admin.manage_recipe('test recipe') == 'Manage recipe'


def test_remove_content():
	admin = Admin('admin')
	assert admin.remove_content('test content') == 'Remove content'


def test_monitor_site_usage():
	admin = Admin('admin')
	assert admin.monitor_site_usage('test usage statistics') == 'Monitor site usage'


def test_monitor_user_engagement():
	admin = Admin('admin')
	assert admin.monitor_user_engagement('test user engagement') == 'Monitor user engagement'
