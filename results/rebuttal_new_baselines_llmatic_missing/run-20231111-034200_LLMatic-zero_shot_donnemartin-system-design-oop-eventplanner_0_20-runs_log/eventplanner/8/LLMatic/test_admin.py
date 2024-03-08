from admin import Admin

def test_admin():
	admin = Admin()

	# Test monitor_user_activities
	assert admin.monitor_user_activities('user1') == 'No activities found'

	# Test analyze_system_performance
	assert admin.analyze_system_performance() == 'System is performing well'

	# Test manage_vendor_listings
	admin.manage_vendor_listings('vendor1', 'add')
	assert admin.manage_vendor_listings('vendor1', 'add') == 'Vendor added'
	admin.manage_vendor_listings('vendor1', 'remove')
	assert admin.manage_vendor_listings('vendor1', 'remove') == 'Vendor not found'
