import pytest
from admin import Admin
from user import User
from shortener import Shortener
from analytics import Analytics


def test_admin():
	shortener = Shortener()
	admin = Admin('admin', shortener)
	user = User('user')
	analytics = Analytics()

	# Test view all urls
	short_url = shortener.shorten_url('https://example.com')
	assert admin.view_all_urls() == {short_url: 'https://example.com'}

	# Test delete url
	admin.delete_url(short_url)
	assert admin.view_all_urls() == {}

	# Test delete user
	user.add_url(short_url, 'https://example.com')
	admin.delete_user(user.username)
	assert admin.view_all_urls() == {}

	# Test monitor system
	short_url = shortener.shorten_url('https://example.com')
	analytics.track_click(short_url, 'USA')
	assert admin.monitor_system(analytics) == {'total_urls': 1, 'total_clicks': 1}

