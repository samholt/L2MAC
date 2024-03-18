import pytest
from url_shortener import URLShortener
import datetime
import time


def test_generate_short_url():
	url_shortener = URLShortener()
	short_url = url_shortener.generate_short_url('https://www.google.com')
	assert len(short_url) == 10
	assert url_shortener.get_original_url(short_url) == 'https://www.google.com'

	# Test with expiration date
	expiration_date = datetime.datetime.now() + datetime.timedelta(seconds=1)
	short_url = url_shortener.generate_short_url('https://www.github.com', expiration_date=expiration_date)
	assert url_shortener.get_original_url(short_url) == 'https://www.github.com'
	# Wait for the URL to expire
	time.sleep(2)
	assert url_shortener.get_original_url(short_url) is None


def test_get_original_url():
	url_shortener = URLShortener()
	short_url = url_shortener.generate_short_url('https://www.google.com')
	assert url_shortener.get_original_url(short_url) == 'https://www.google.com'
	assert url_shortener.get_original_url('invalid') is None


def test_get_all_urls():
	url_shortener = URLShortener()
	url_shortener.generate_short_url('https://www.google.com')
	url_shortener.generate_short_url('https://www.github.com')
	all_urls = url_shortener.get_all_urls()
	assert len(all_urls) == 2


def test_delete_url():
	url_shortener = URLShortener()
	short_url = url_shortener.generate_short_url('https://www.google.com')
	url_shortener.delete_url(short_url)
	assert url_shortener.get_original_url(short_url) is None


def test_validate_url():
	url_shortener = URLShortener()
	assert url_shortener.validate_url('https://www.google.com') is True
	assert url_shortener.validate_url('invalid') is False
