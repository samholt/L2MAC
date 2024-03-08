import pytest
from admin_dashboard import AdminDashboard

def test_admin_dashboard():
	admin = AdminDashboard()
	admin.monitor_user_activities('user1', 'login')
	assert admin.user_activities['user1'] == 'login'
	admin.manage_platform_content('content1', 'add')
	assert admin.platform_content['content1'] == 'active'
	admin.manage_platform_content('content1', 'remove')
	assert 'content1' not in admin.platform_content
