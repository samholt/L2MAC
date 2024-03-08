import admin

def test_monitor_user_activities():
	admin_obj = admin.Admin()
	admin_obj.monitor_user_activities('user1', 'activity1')
	assert admin_obj.user_activities['user1'] == 'activity1'

def test_manage_vendor_listings():
	admin_obj = admin.Admin()
	admin_obj.manage_vendor_listings('vendor1', 'listing1')
	assert admin_obj.vendor_listings['vendor1'] == 'listing1'

def test_manage_platform_content():
	admin_obj = admin.Admin()
	admin_obj.manage_platform_content('content1', 'content2')
	assert admin_obj.platform_content['content1'] == 'content2'
