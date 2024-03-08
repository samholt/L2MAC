import admin

def test_monitor_user_activities():
	admin_obj = admin.Admin()
	admin_obj.monitor_user_activities('user1', 'activity1')
	assert admin_obj.user_activities['user1'] == 'activity1'

def test_manage_system_performance():
	admin_obj = admin.Admin()
	admin_obj.manage_system_performance({'cpu': 'low'})
	assert admin_obj.system_performance['cpu'] == 'low'

def test_manage_vendor_listings():
	admin_obj = admin.Admin()
	admin_obj.manage_vendor_listings('vendor1', 'listing1')
	assert admin_obj.vendor_listings['vendor1'] == 'listing1'

