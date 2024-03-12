import pytest
from admin import Admin


def test_admin():
	admin = Admin('admin', 'admin')

	# Test view_all_urls method
	assert admin.view_all_urls() == {}

	# Test delete_url method
	admin.all_urls = {'google.com': 'goo.gl'}
	admin.delete_url('google.com')
	assert admin.all_urls == {}

	# Test delete_user method
	admin.all_users = {'user1': 'password1'}
	admin.delete_user('user1')
	assert admin.all_users == {}

	# Test monitor_system method
	# In a real-world application, this method would return system performance and analytics
	# Here, we'll just print a message
	admin.monitor_system()

