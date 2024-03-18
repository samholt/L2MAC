import pytest
from url_shortener import URLShortener
from datetime import datetime, timedelta
import time


def test_shorten_url():
	url_shortener = URLShortener()
	short_url = url_shortener.shorten_url('https://www.google.com')
	assert len(short_url) == 6
	assert url_shortener.get_long_url(short_url) == 'https://www.google.com'


def test_invalid_url():
	url_shortener = URLShortener()
	result = url_shortener.shorten_url('invalid_url')
	assert result is None


def test_analytics():
	url_shortener = URLShortener()
	short_url = url_shortener.shorten_url('https://www.google.com')
	url_shortener.get_long_url(short_url)
	analytics = url_shortener.get_analytics(short_url)
	assert analytics['clicks'] == 1
	assert len(analytics['click_details']) == 1


def test_url_expiration():
	url_shortener = URLShortener()
	expiration = datetime.now() + timedelta(seconds=1)
	short_url = url_shortener.shorten_url('https://www.google.com', expiration=expiration)
	assert url_shortener.get_long_url(short_url) == 'https://www.google.com'
	time.sleep(2)
	assert url_shortener.get_long_url(short_url) is None
