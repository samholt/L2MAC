import url_shortener
from datetime import datetime, timedelta


def test_generate_short_url():
	"""Test the generate_short_url function."""
	url = 'https://www.example.com'
	short_url, expiration_datetime = url_shortener.generate_short_url(url, expiration_time=10)
	assert len(short_url) == 10
	assert short_url.isalnum()
	assert expiration_datetime > datetime.now()

	custom_short_url = 'custom'
	custom_url, custom_expiration_datetime = url_shortener.generate_short_url(url, custom_short_url, expiration_time=10)
	assert custom_url == custom_short_url
	assert custom_expiration_datetime > datetime.now()


def test_validate_url():
	"""Test the validate_url function."""
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url)
	assert not url_shortener.validate_url(invalid_url)
