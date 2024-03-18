import pytest
from shortener import Shortener
import datetime
import time


def test_shorten_url():
	shortener = Shortener()
	url1 = 'https://www.google.com'
	url2 = 'https://www.facebook.com'
	short_url1 = shortener.shorten_url(url1)
	short_url2 = shortener.shorten_url(url2)
	assert len(short_url1) == 6
	assert len(short_url2) == 6
	assert short_url1 != short_url2


def test_validate_url():
	shortener = Shortener()
	valid_url = 'https://www.google.com'
	invalid_url = 'https://www.invalidurl.com'
	assert shortener.validate_url(valid_url) is True
	assert shortener.validate_url(invalid_url) is False


def test_url_expiration():
	shortener = Shortener()
	url = 'https://www.google.com'
	expiration = datetime.datetime.now() + datetime.timedelta(seconds=1)
	short_url = shortener.shorten_url(url, expiration)
	time.sleep(2)
	assert shortener.get_original_url(short_url) is None

