import pytest
from admin_dashboard import AdminDashboard

def test_create_dashboard():
	admin_dashboard = AdminDashboard(None, None)
	admin_dashboard.create_dashboard('1', 'admin1')
	assert admin_dashboard.id == '1'
	assert admin_dashboard.admin_user == 'admin1'

def test_add_moderation_tool():
	admin_dashboard = AdminDashboard('1', 'admin1')
	admin_dashboard.add_moderation_tool('tool1')
	assert 'tool1' in admin_dashboard.moderation_tools

def test_update_dashboard():
	admin_dashboard = AdminDashboard('1', 'admin1')
	admin_dashboard.update_dashboard('2', 'admin2')
	assert admin_dashboard.id == '2'
	assert admin_dashboard.admin_user == 'admin2'
