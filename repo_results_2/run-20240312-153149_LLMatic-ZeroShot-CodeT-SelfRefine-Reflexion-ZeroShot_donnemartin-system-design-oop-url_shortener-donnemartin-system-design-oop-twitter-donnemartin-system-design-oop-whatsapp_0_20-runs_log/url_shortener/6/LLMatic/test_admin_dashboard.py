import pytest
from admin_dashboard import AdminDashboard


def test_admin_dashboard():
	admin = AdminDashboard()

	# Test view all urls
	assert admin.view_all_urls() == []

	# Test delete url
	assert admin.delete_url('user1', 'url1') == False

	# Test delete user
	assert admin.delete_user('user1') == False

	# Test view system performance
	assert admin.view_system_performance() == (0, 0)

	# Test view analytics
	assert admin.view_analytics('url1') == []
