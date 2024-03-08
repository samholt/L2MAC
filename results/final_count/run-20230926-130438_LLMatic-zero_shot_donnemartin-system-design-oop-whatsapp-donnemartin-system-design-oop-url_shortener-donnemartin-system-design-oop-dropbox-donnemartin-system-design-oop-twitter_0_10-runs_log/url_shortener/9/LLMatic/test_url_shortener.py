import pytest
from url_shortener import URLShortener
from datetime import datetime, timedelta


def test_url_validation():
	url_shortener = URLShortener()
	assert url_shortener.validate_url('https://www.google.com') == True
	assert url_shortener.validate_url('invalid_url') == False


def test_generate_short_url():
	url_shortener = URLShortener()
	short_url = url_shortener.generate_short_url('https://www.google.com')
	assert len(short_url) == 6
	assert short_url.isalnum() == True


def test_custom_short_url():
	url_shortener = URLShortener()
	custom_url = 'custom'
	assert url_shortener.custom_short_url('https://www.google.com', custom_url) == custom_url
	assert url_shortener.custom_short_url('https://www.google.com', custom_url) == 'Custom URL already exists'


def test_url_expiration():
	url_shortener = URLShortener()
	short_url = url_shortener.generate_short_url('https://www.google.com', expiration_minutes=1)
	assert url_shortener.get_original_url(short_url) == 'https://www.google.com'
	# Simulate time passing
	url_shortener.url_dict['https://www.google.com']['expiration_time'] = datetime.now() - timedelta(minutes=1)
	assert url_shortener.get_original_url(short_url) == 'URL expired'
