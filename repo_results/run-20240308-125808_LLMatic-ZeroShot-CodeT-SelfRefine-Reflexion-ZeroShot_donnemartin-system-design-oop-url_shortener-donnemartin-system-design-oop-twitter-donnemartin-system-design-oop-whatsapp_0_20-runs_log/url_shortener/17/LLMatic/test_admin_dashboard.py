import pytest
from admin_dashboard import AdminDashboard
from user_accounts import UserAccounts


def test_admin_dashboard():
	url_db = {'abc': 'http://example.com'}
	user_accounts = UserAccounts()
	user_accounts.create_account('testuser')
	user_accounts.add_url('testuser', 'http://example.com')
	admin_dashboard = AdminDashboard(url_db, user_accounts)

	# Test view_all_urls
	assert admin_dashboard.view_all_urls() == {'abc': 'http://example.com'}

	# Test delete_url
	assert admin_dashboard.delete_url('abc') == 'URL deleted successfully.'
	assert admin_dashboard.delete_url('abc') == 'URL does not exist.'

	# Test delete_user
	assert admin_dashboard.delete_user('testuser') == 'User deleted successfully.'
	assert admin_dashboard.delete_user('testuser') == 'User does not exist.'

	# Test monitor_system
	assert admin_dashboard.monitor_system() == {'url_count': 0, 'user_count': 0}
