import pytest
from admin_dashboard import AdminDashboard


def test_admin_dashboard():
	admin = AdminDashboard()

	# Test view all urls
	assert admin.view_all_urls() == []

	# Test delete url
	assert admin.delete_url('http://short.url') == 'URL not found.'

	# Test delete user
	assert admin.delete_user('user1') == 'User not found.'

	# Test view analytics
	assert admin.view_analytics() == {}
