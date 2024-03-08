import pytest
from user import User
from shortener import Shortener


def test_create_account():
	shortener = Shortener()
	user1 = User('testuser', 'password', shortener)
	assert user1.create_account() == {'username': 'testuser', 'password': 'password'}


def test_view_urls():
	shortener = Shortener()
	user1 = User('testuser', 'password', shortener)
	assert isinstance(user1.view_urls(), dict)


def test_edit_url():
	shortener = Shortener()
	user1 = User('testuser', 'password', shortener)
	short_url = shortener.shorten_url('https://www.google.com')
	user1.urls[short_url] = 'https://www.google.com'
	assert user1.edit_url(short_url, 'https://www.example.com') is True


def test_delete_url():
	shortener = Shortener()
	user1 = User('testuser', 'password', shortener)
	short_url = shortener.shorten_url('https://www.google.com')
	user1.urls[short_url] = 'https://www.google.com'
	assert user1.delete_url(short_url) is True


def test_view_analytics():
	shortener = Shortener()
	user1 = User('testuser', 'password', shortener)
	short_url = shortener.shorten_url('https://www.google.com')
	user1.urls[short_url] = 'https://www.google.com'
	assert isinstance(user1.view_analytics(), dict)


def test_set_expiration():
	shortener = Shortener()
	user1 = User('testuser', 'password', shortener)
	short_url = shortener.shorten_url('https://www.google.com')
	user1.set_expiration(short_url, '2022-12-31T23:59:59')
	assert shortener.get_original_url(short_url) is None

