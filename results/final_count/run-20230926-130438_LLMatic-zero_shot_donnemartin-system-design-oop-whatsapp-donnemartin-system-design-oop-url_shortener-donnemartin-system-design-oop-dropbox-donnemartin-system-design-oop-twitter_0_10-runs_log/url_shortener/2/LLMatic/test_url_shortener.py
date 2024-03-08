import url_shortener
from datetime import datetime, timedelta
import time


def test_generate_short_url():
	"""Test the generate_short_url function."""
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert isinstance(short_url, str)


def test_validate_url():
	"""Test the validate_url function."""
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url) is True
	assert url_shortener.validate_url(invalid_url) is False


def test_url_expiration():
	"""Test that URLs expire correctly."""
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url, expiration_minutes=0)
	assert url_shortener.get_original_url(short_url) is None
	
	short_url = url_shortener.generate_short_url(url, expiration_minutes=1)
	assert url_shortener.get_original_url(short_url) == url
	
	# Wait for the URL to expire
	time.sleep(61)
	assert url_shortener.get_original_url(short_url) is None
