import pytest
from admin_dashboard import AdminDashboard


def test_admin_dashboard():
	url_database = {'abc123': 'http://example.com'}
	user_database = {'user1': {'abc123': 'http://example.com'}}
	analytics = {'abc123': {'clicks': 10}}

	admin = AdminDashboard(url_database, user_database)

	assert admin.view_all_urls() == url_database

	admin.delete_url('abc123')
	assert 'abc123' not in url_database

	admin.delete_user('user1')
	assert 'user1' not in user_database

	assert admin.monitor_system(analytics) == analytics
