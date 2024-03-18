import pytest
from url_shortener import generate_short_url, validate_url, set_expiration
from datetime import datetime, timedelta


def test_generate_short_url():
	url = 'https://www.google.com'
	short_url = generate_short_url(url)
	assert len(short_url) == 10


def test_validate_url():
	valid_url = 'https://www.google.com'
	invalid_url = 'https://www.invalidurl.com'
	assert validate_url(valid_url) == True
	assert validate_url(invalid_url) == False


def test_set_expiration():
	short_url = '1234567890'
	expiration = set_expiration(short_url)
	assert isinstance(expiration, datetime)
	assert expiration > datetime.now()
	assert expiration < datetime.now() + timedelta(hours=24)
