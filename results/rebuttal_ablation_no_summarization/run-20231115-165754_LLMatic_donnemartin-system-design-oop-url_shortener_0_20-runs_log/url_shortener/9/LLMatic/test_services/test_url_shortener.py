import pytest
from services.url_shortener import UrlShortener
import datetime


def test_url_shortener():
	url_shortener = UrlShortener()

	# Test URL validation
	assert url_shortener.validate_url('https://www.google.com')
	assert not url_shortener.validate_url('invalid_url')

	# Test URL shortening
	short_url = url_shortener.create_short_url('https://www.google.com')
	assert len(short_url) == 6
	assert url_shortener.get_original_url(short_url) == 'https://www.google.com'

	# Test custom alias
	custom_alias = 'custom'
	assert url_shortener.create_short_url('https://www.google.com', custom_alias=custom_alias) == custom_alias
	assert url_shortener.get_original_url(custom_alias) == 'https://www.google.com'

	# Test URL expiration
	expired_url = url_shortener.create_short_url('https://www.google.com', expiration_date=datetime.datetime.now() - datetime.timedelta(minutes=1))
	assert url_shortener.get_original_url(expired_url) == 'URL expired'
