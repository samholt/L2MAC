import url_shortener
from datetime import datetime, timedelta
import time


def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert short_url != url

	custom_short_url = 'custom'
	custom_url = url_shortener.generate_short_url(url, custom_short_url)
	assert custom_url == custom_short_url


def test_validate_url():
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url) is True
	assert url_shortener.validate_url(invalid_url) is False


def test_url_expiration():
	url = 'https://www.example.com'
	expiration = datetime.now() + timedelta(seconds=1)
	short_url = url_shortener.generate_short_url(url, expiration=expiration)

	# URL should be active immediately after creation
	assert url_shortener.get_url(short_url) == url

	# Wait for URL to expire
	time.sleep(2)

	# URL should be inactive after expiration
	assert url_shortener.get_url(short_url) is None
