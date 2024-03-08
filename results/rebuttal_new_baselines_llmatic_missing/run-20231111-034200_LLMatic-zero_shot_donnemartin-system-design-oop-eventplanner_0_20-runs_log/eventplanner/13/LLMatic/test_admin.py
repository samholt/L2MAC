import pytest
from admin import Admin

admin_manager = Admin()

def test_add_admin():
	admin_manager.add_admin('admin1', {'name': 'Admin 1'})
	assert 'admin1' in admin_manager.admins

def test_monitor_user_activities():
	assert admin_manager.monitor_user_activities('user1') == 'Monitoring user activities'

def test_view_system_performance():
	assert admin_manager.view_system_performance() == 'Viewing system performance'

def test_view_user_engagement():
	assert admin_manager.view_user_engagement() == 'Viewing user engagement'

def test_manage_vendor_listings():
	assert admin_manager.manage_vendor_listings('vendor1') == 'Managing vendor listings'

def test_manage_platform_content():
	assert admin_manager.manage_platform_content('content1') == 'Managing platform content'
