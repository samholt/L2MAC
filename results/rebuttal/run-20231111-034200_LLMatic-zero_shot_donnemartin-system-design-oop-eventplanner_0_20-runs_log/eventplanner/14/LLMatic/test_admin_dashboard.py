import admin_dashboard

def test_monitor_user_activities():
	admin = admin_dashboard.AdminDashboard()
	assert admin.monitor_user_activities('user1') == {'login': '2022-01-01', 'logout': '2022-01-02'}

def test_manage_user_activities():
	admin = admin_dashboard.AdminDashboard()
	assert admin.manage_user_activities('user1', {'login': '2022-01-03', 'logout': '2022-01-04'}) == {'login': '2022-01-03', 'logout': '2022-01-04'}

def test_manage_vendor_listings():
	admin = admin_dashboard.AdminDashboard()
	assert admin.manage_vendor_listings('vendor1', 'listing1') == 'listing1'

def test_manage_platform_content():
	admin = admin_dashboard.AdminDashboard()
	assert admin.manage_platform_content('content1') == 'content1'
