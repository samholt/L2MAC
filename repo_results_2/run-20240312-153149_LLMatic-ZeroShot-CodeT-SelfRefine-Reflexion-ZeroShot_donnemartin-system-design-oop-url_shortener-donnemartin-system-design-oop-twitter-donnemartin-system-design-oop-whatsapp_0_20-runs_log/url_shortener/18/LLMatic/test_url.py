import pytest
from datetime import datetime, timedelta
from url import URL
from user import User
from database import Database


def test_url_creation():
	user = User('test_user', 'password')
	url = URL('http://test.com', user)
	assert url is not None
	assert url.original_url == 'http://test.com'
	assert url.user == user


def test_url_validation():
	user = User('test_user', 'password')
	valid_url = URL('http://test.com', user)
	invalid_url = URL('invalid', user)
	assert valid_url.is_valid() is True
	assert invalid_url.is_valid() is False


def test_url_expiration():
	user = User('test_user', 'password')
	expired_url = URL('http://test.com', user, expiration_date=datetime.now() - timedelta(days=1))
	not_expired_url = URL('http://test.com', user, expiration_date=datetime.now() + timedelta(days=1))
	assert expired_url.is_expired() is True
	assert not_expired_url.is_expired() is False


def test_url_redirection():
	user = User('test_user', 'password')
	url = URL('http://test.com', user)
	assert url.redirect() == 'http://test.com'


def test_get_original_url():
	db = Database()
	user = User('test_user', 'password')
	url = URL('http://test.com', user)
	db.add_url(url)
	assert db.get_original_url(url.short_url) == 'http://test.com'
