import pytest
from shortener import Shortener
import time


def test_validate_url():
	shortener = Shortener()
	assert shortener.validate_url('https://www.google.com')
	assert not shortener.validate_url('invalid_url')


def test_generate_short_url():
	shortener = Shortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	assert short_url in shortener.url_map
	assert shortener.url_map[short_url] == url

	custom_alias = 'custom'
	custom_short_url = shortener.generate_short_url(url, custom_alias=custom_alias)
	assert custom_short_url == custom_alias
	assert custom_alias in shortener.url_map
	assert shortener.url_map[custom_alias] == url


def test_get_original_url():
	shortener = Shortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	assert shortener.get_original_url(short_url) == url
	assert shortener.get_original_url('invalid') is None


def test_url_expiration():
	shortener = Shortener()
	url = 'https://www.google.com'
	expiry_time = time.time() + 1
	short_url = shortener.generate_short_url(url, expiry_time=expiry_time)
	time.sleep(2)
	assert shortener.get_original_url(short_url) is None
