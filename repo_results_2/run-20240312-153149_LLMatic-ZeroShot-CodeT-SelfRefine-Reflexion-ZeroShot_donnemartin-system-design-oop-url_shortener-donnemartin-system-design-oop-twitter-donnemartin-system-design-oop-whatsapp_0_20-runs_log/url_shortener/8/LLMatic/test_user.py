import pytest
from user import User
from url_shortener import URLShortener


def test_user_creation():
	user = User('testuser', 'password')
	assert user.username == 'testuser'
	assert user.password == 'password'


def test_user_account_creation():
	user = User('testuser', 'password')
	url_shortener = URLShortener()
	user.create_account(url_shortener)
	assert 'testuser' in url_shortener.users


def test_user_url_shortening():
	user = User('testuser', 'password')
	url_shortener = URLShortener()
	user.create_account(url_shortener)
	short_url = user.add_url('https://www.google.com', url_shortener)
	assert short_url in user.urls
	assert user.urls[short_url] == 'https://www.google.com'


def test_user_url_editing():
	user = User('testuser', 'password')
	url_shortener = URLShortener()
	user.create_account(url_shortener)
	short_url = user.add_url('https://www.google.com', url_shortener)
	user.edit_url(short_url, 'https://www.bing.com', url_shortener)
	assert user.urls[short_url] == 'https://www.bing.com'


def test_user_url_deletion():
	user = User('testuser', 'password')
	url_shortener = URLShortener()
	user.create_account(url_shortener)
	short_url = user.add_url('https://www.google.com', url_shortener)
	user.delete_url(short_url, url_shortener)
	assert short_url not in user.urls


def test_user_view_analytics():
	user = User('testuser', 'password')
	url_shortener = URLShortener()
	user.create_account(url_shortener)
	short_url = user.add_url('https://www.google.com', url_shortener)
	analytics = user.view_analytics(short_url, url_shortener)
	assert isinstance(analytics, dict)
