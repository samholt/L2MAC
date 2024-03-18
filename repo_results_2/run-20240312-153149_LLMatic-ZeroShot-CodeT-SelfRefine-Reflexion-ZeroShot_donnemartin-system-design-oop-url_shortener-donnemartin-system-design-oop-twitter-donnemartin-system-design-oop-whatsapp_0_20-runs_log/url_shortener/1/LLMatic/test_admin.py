import pytest
from admin import Admin
from user import User


def test_admin_features():
	users_db = {}
	admin = Admin('admin', 'admin')
	user1 = User('user1', 'password1')
	user2 = User('user2', 'password2')

	# Create user accounts
	user1.create_account(users_db)
	user2.create_account(users_db)

	# Admin views all URLs
	assert admin.view_all_urls(users_db) == {}

	# Users add URLs
	user1.urls['url1'] = 'short_url1'
	user2.urls['url2'] = 'short_url2'

	# Admin views all URLs
	assert admin.view_all_urls(users_db) == {'url1': 'short_url1', 'url2': 'short_url2'}

	# Admin deletes a URL
	assert admin.delete_url('url1', users_db) == 'URL deleted successfully'
	assert 'url1' not in user1.urls

	# Admin deletes a user
	assert admin.delete_user('user2', users_db) == 'User deleted successfully'
	assert 'user2' not in users_db

	# Admin views system performance
	assert admin.view_system_performance(users_db) == {'total_users': 1, 'total_urls': 0}
