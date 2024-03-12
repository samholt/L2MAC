import url_shortener
from datetime import datetime, timedelta
import time


def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert short_url.isalnum()

	# Test custom short link
	custom_short_link = 'custom'
	short_url = url_shortener.generate_short_url(url, custom_short_link)
	assert short_url == custom_short_link

	# Test that the same custom short link cannot be used again
	short_url = url_shortener.generate_short_url(url, custom_short_link)
	assert short_url != custom_short_link


def test_validate_url():
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url) is True
	assert url_shortener.validate_url(invalid_url) is False


def test_url_expiration():
	# Test URL expiration
	url = 'https://www.example.com'
	expiration_time = datetime.now() + timedelta(seconds=1)
	short_url = url_shortener.generate_short_url(url, expiration_time=expiration_time)
	assert url_shortener.is_url_expired(short_url) is False
	# Wait for the URL to expire
	time.sleep(2)
	assert url_shortener.is_url_expired(short_url) is True
