import pytest
from admin import Admin
from shortener import Shortener


def test_view_all_urls():
	shortener = Shortener()
	admin1 = Admin('testadmin', 'password', shortener, {})
	assert isinstance(admin1.view_all_urls(), dict)


def test_delete_url():
	shortener = Shortener()
	admin1 = Admin('testadmin', 'password', shortener, {})
	short_url = shortener.shorten_url('https://www.google.com')
	assert admin1.delete_url(short_url) is True


def test_delete_user():
	shortener = Shortener()
	admin1 = Admin('testadmin', 'password', shortener, {'testuser': None})
	assert admin1.delete_user('testuser') is True


def test_monitor_system():
	shortener = Shortener()
	admin1 = Admin('testadmin', 'password', shortener, {})
	assert isinstance(admin1.monitor_system(), dict)

