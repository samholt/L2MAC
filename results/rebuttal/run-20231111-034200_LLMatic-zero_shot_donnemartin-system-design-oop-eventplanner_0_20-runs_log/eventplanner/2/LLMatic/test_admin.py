import pytest
from admin import Admin


def test_monitor_and_get_user_activities():
	admin = Admin()
	admin.monitor_user_activities('user1', 'login')
	admin.monitor_user_activities('user1', 'logout')
	activities = admin.get_user_activities('user1')
	assert activities == ['login', 'logout']


def test_update_and_get_system_performance():
	admin = Admin()
	admin.update_system_performance('CPU', 90)
	performance = admin.get_system_performance()
	assert performance == {'CPU': 90}


def test_manage_and_get_vendor_listings():
	admin = Admin()
	admin.manage_vendor_listings('vendor1', 'listing1')
	listing = admin.get_vendor_listings('vendor1')
	assert listing == 'listing1'
