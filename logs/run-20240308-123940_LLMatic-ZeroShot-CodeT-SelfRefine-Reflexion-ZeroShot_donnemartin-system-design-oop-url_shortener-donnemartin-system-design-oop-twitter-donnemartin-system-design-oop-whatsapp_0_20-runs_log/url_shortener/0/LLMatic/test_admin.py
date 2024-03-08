import pytest
from admin import Admin
from shortener import Shortener
from user import User


def test_admin():
	shortener = Shortener()
	user = User()
	admin = Admin(shortener, user)

	# Test view all urls
	assert admin.view_all_urls() == {}

	# Test delete url
	short_url = shortener.generate_short_url('https://example.com')
	assert admin.delete_url(short_url) == True
	assert short_url not in shortener.url_map

	# Test delete user
	user.register('test', 'password')
	assert admin.delete_user('test') == True
	assert 'test' not in user.users

	# Test monitor system
	monitor = admin.monitor_system()
	assert monitor['users'] == 0
	assert monitor['urls'] == 0
