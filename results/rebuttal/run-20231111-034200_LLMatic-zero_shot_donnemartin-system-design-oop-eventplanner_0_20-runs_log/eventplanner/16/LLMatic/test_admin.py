import pytest
from admin import Admin, admins

def test_admin_functions():
	admin = Admin('1', 'Admin1')
	admins['1'] = admin

	admin.monitor_user_activities('user1', 'activity1')
	assert admins['1'].user_activities['user1'] == 'activity1'

	admin.manage_user_activities('user1', 'activity2')
	assert admins['1'].user_activities['user1'] == 'activity2'

	admin.manage_vendor_listings('vendor1', 'listing1')
	assert admins['1'].platform_content['vendor1'] == 'listing1'

	admin.manage_platform_content('content1', 'content1')
	assert admins['1'].platform_content['content1'] == 'content1'

