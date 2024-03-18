import pytest
from admin import Admin
from database import Database
from user import User
from url import URL


def test_admin():
	db = Database()
	admin = Admin(db)

	# Add a user and a URL
	user = User('test_user', 'password')
	url = URL('https://example.com', 'exmpl', user)
	db.add_user(user)
	db.add_url(url)

	# Test view_all_urls
	assert len(admin.view_all_urls()) == 1

	# Test delete_url
	admin.delete_url('exmpl')
	assert 'exmpl' not in [url.short_url for url in admin.view_all_urls()]

	# Test delete_user
	admin.delete_user('test_user')
	assert 'test_user' not in db.users

	# Test monitor_system
	monitor_data = admin.monitor_system()
	assert monitor_data['user_count'] == 0
	assert monitor_data['url_count'] == 1

	# Add a user and a URL again
	user = User('test_user2', 'password')
	url = URL('https://example2.com', 'exmpl2', user)
	db.add_user(user)
	db.add_url(url)

	# Test monitor_system again
	monitor_data = admin.monitor_system()
	assert monitor_data['user_count'] == 1
	assert monitor_data['url_count'] == 2
