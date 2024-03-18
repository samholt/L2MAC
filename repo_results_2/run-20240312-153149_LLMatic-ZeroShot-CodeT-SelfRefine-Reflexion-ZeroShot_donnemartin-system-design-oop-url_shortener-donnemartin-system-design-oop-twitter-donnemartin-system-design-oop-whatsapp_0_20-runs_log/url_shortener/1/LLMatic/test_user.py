import pytest
from user import User
from shortener import Shortener

users_db = {}

def test_create_account():
	user = User('testuser', 'testpassword')
	assert user.create_account(users_db) == 'Account created successfully'
	assert user.create_account(users_db) == {'error': 'Username already exists'}


def test_view_urls():
	user = User('testuser', 'testpassword')
	assert user.view_urls() == {}


def test_edit_url():
	user = User('testuser', 'testpassword')
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	user.urls[short_url] = shortener
	assert user.edit_url(short_url, 'https://www.bing.com') == 'URL edited successfully'
	assert user.edit_url('https://www.yahoo.com', 'https://www.bing.com') == {'error': 'URL not found'}


def test_delete_url():
	user = User('testuser', 'testpassword')
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	user.urls[short_url] = shortener
	assert user.delete_url(short_url) == 'URL deleted successfully'
	assert user.delete_url('https://www.yahoo.com') == {'error': 'URL not found'}


def test_view_analytics():
	user = User('testuser', 'testpassword')
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	user.urls[short_url] = shortener
	assert isinstance(user.view_analytics(), dict)
