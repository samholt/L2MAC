import pytest
from shortener import Shortener
from datetime import datetime, timedelta


def test_shorten_url():
	shortener = Shortener()

	url1 = 'https://www.google.com'
	url2 = 'https://www.facebook.com'

	short_url1 = shortener.shorten_url(url1, expiration_date=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S'))
	short_url2 = shortener.shorten_url(url2, expiration_date=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S'))

	assert len(short_url1) == 10
	assert len(short_url2) == 10
	assert short_url1 != short_url2
	assert shortener.url_dict[short_url1]['url'] == url1
	assert shortener.url_dict[short_url2]['url'] == url2

	custom_short_link = 'custom'
	assert shortener.shorten_url(url1, custom_short_link, expiration_date=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')) == custom_short_link
	assert shortener.url_dict[custom_short_link]['url'] == url1
	assert shortener.shorten_url(url1, custom_short_link, expiration_date=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')) == 'Custom short link already in use'


def test_validate_url():
	shortener = Shortener()

	assert shortener.validate_url('https://www.google.com')
	assert not shortener.validate_url('https://www.invalidurl.com')


def test_is_expired():
	shortener = Shortener()

	# Test with a URL that has not expired
	short_url = shortener.shorten_url('https://www.google.com', expiration_date=(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S'))
	assert not shortener.is_expired(short_url)

	# Test with a URL that has expired
	short_url = shortener.shorten_url('https://www.facebook.com', expiration_date=(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S'))
	assert shortener.is_expired(short_url)
