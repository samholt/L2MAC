import pytest
from admin_dashboard import AdminDashboard


def test_admin_dashboard():
	admin = AdminDashboard()

	# Test view all URLs
	assert admin.view_all_urls() == []

	# Test delete URL
	admin.user_account.create_account('test_user')
	admin.user_account.users['test_user'].append('test_url')
	assert admin.delete_url('test_user', 'test_url') == 'URL deleted successfully.'
	assert admin.delete_url('test_user', 'test_url') == 'URL does not exist.'

	# Test delete user
	assert admin.delete_user('test_user') == 'User deleted successfully.'
	assert admin.delete_user('test_user') == 'Username does not exist.'

	# Test monitor system
	admin.user_account.create_account('test_user2')
	admin.user_account.users['test_user2'].append('test_url2')
	assert admin.monitor_system() == {'total_users': 1, 'total_urls': 1}
