import pytest
from url_shortener import URLShortener
from database import Database
from datetime import datetime, timedelta

def test_url_shortener():
	db = Database()
	url_shortener = URLShortener(db)

	# Test URL validation
	assert url_shortener.validate_url('https://www.google.com')
	assert not url_shortener.validate_url('invalid_url')

	# Test URL shortening
	original_url = 'https://www.google.com'
	expiration_date = datetime.now() + timedelta(days=1)
	short_url = url_shortener.shorten_url(original_url, expiration_date)
	assert db.get('urls', short_url)['url'] == original_url

	# Test custom short URL
	custom_short_url = 'custom'
	assert url_shortener.shorten_url(original_url, expiration_date, custom_short_url) == custom_short_url
	assert db.get('urls', custom_short_url)['url'] == original_url

	# Test that an error is returned when a custom short URL is already in use
	assert url_shortener.shorten_url(original_url, expiration_date, custom_short_url) == 'Custom short URL already in use'

	# Test URL expiration
	expired_url = url_shortener.shorten_url(original_url, datetime.now() - timedelta(days=1))
	assert url_shortener.get_original_url(expired_url) is None
