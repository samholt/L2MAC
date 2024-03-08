import pytest
from admin_dashboard import AdminDashboard

def test_admin_dashboard():
	admin_dashboard = AdminDashboard()

	admin_dashboard.monitor_user_activities('user1', 'activity1')
	assert admin_dashboard.user_activities['user1'] == 'activity1'

	admin_dashboard.manage_system_performance('metric1', 'value1')
	assert admin_dashboard.system_performance['metric1'] == 'value1'

	admin_dashboard.analyze_user_engagement('user1', 'engagement1')
	assert admin_dashboard.user_engagement['user1'] == 'engagement1'

	admin_dashboard.manage_vendor_listings('vendor1', 'listing1')
	assert admin_dashboard.vendor_listings['vendor1'] == 'listing1'

	admin_dashboard.manage_platform_content('content1', 'content1')
	assert admin_dashboard.platform_content['content1'] == 'content1'
