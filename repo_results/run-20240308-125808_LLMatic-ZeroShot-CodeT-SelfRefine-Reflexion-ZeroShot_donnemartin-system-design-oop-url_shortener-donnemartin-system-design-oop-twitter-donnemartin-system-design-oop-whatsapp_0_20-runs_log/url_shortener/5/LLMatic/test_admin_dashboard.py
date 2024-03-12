from admin_dashboard import AdminDashboard

def test_admin_dashboard():
	admin_dashboard = AdminDashboard()

	# Test view_all_urls
	all_urls = admin_dashboard.view_all_urls()
	assert isinstance(all_urls, dict)

	# Test delete_url
	admin_dashboard.delete_url('test_url_id')
	assert 'test_url_id' not in admin_dashboard.view_all_urls()

	# Test delete_user
	admin_dashboard.delete_user('test_user_id')
	assert 'test_user_id' not in admin_dashboard.user_account.get_all_users()

	# Test monitor_system
	monitor_result = admin_dashboard.monitor_system()
	assert isinstance(monitor_result, dict)
	assert 'system_performance' in monitor_result
	assert 'analytics' in monitor_result
