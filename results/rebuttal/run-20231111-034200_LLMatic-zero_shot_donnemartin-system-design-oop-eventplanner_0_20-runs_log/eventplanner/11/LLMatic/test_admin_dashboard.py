import pytest
from admin_dashboard import AdminDashboard


def test_monitor_user_activities():
	admin_dashboard = AdminDashboard()
	result = admin_dashboard.monitor_user_activities('user1', 'login')
	assert result == {'user1': ['login']}


def test_manage_system_performance():
	admin_dashboard = AdminDashboard()
	result = admin_dashboard.manage_system_performance('CPU', '80%')
	assert result == {'CPU': '80%'}


def test_manage_vendor_listings():
	admin_dashboard = AdminDashboard()
	result = admin_dashboard.manage_vendor_listings('vendor1', 'listing1')
	assert result == {'vendor1': 'listing1'}
