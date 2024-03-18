import pytest
from shortener import Shortener
from datetime import datetime, timedelta


def test_shortener():
	shortener = Shortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	assert shortener.get_original_url(short_url) == url
	assert shortener.get_analytics(short_url) == {'clicks': 0, 'click_data': []}

	shortener.get_original_url(short_url, '127.0.0.1')
	analytics = shortener.get_analytics(short_url)
	assert analytics['clicks'] == 1
	assert len(analytics['click_data']) == 1
	assert analytics['click_data'][0]['ip_address'] == '127.0.0.1'

	shortener.get_original_url(short_url, '127.0.0.2')
	analytics = shortener.get_analytics(short_url)
	assert analytics['clicks'] == 2
	assert len(analytics['click_data']) == 2
	assert analytics['click_data'][1]['ip_address'] == '127.0.0.2'

	# Test URL expiration
	expired_url = 'https://www.expired.com'
	expiration_date = datetime.now() - timedelta(days=1)  # Set expiration date to yesterday
	expired_short_url = shortener.generate_short_url(expired_url, expiration_date=expiration_date)
	assert shortener.get_original_url(expired_short_url) is None

	valid_url = 'https://www.valid.com'
	expiration_date = datetime.now() + timedelta(days=1)  # Set expiration date to tomorrow
	valid_short_url = shortener.generate_short_url(valid_url, expiration_date=expiration_date)
	assert shortener.get_original_url(valid_short_url) == valid_url


def test_invalid_url():
	shortener = Shortener()
	assert shortener.generate_short_url('invalid_url') is None
