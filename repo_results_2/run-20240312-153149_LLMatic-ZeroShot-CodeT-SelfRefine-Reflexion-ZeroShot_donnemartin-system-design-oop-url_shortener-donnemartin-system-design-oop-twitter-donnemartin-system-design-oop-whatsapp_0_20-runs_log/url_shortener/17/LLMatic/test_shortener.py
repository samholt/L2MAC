import pytest
from shortener import Shortener
from models import URL


def test_shorten_url():
	shortener = Shortener()
	url = 'https://www.google.com'
	short_url = shortener.shorten_url(url)
	assert len(short_url) == 10
	assert isinstance(shortener.urls[short_url], URL)
	assert shortener.urls[short_url].original_url == url

	custom_short_url = 'custom'
	custom_url = shortener.shorten_url(url, custom_short_url)
	assert custom_url == custom_short_url
	assert isinstance(shortener.urls[custom_url], URL)
	assert shortener.urls[custom_url].original_url == url


def test_validate_url():
	shortener = Shortener()
	assert shortener.validate_url('https://www.google.com')
	assert not shortener.validate_url('https://www.invalidurl.com')
