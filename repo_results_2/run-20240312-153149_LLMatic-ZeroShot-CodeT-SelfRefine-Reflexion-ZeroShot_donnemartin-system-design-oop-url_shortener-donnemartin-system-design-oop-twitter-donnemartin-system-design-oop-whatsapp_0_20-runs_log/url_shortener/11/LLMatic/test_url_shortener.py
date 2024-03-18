import url_shortener
from datetime import datetime, timedelta
import time


def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert short_url.isalnum()


def test_generate_custom_short_url():
	url = 'https://www.example.com'
	custom_short_link = 'custom'
	short_url = url_shortener.generate_short_url(url, custom_short_link)
	assert short_url == custom_short_link


def test_validate_url():
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url) is True
	assert url_shortener.validate_url(invalid_url) is False


def test_url_expiration():
	url = 'https://www.example.com'
	expiration_date = datetime.now() + timedelta(seconds=1)
	short_url = url_shortener.generate_short_url(url, expiration_date=expiration_date)
	assert url_shortener.is_url_expired(short_url) is False
	time.sleep(2)
	assert url_shortener.is_url_expired(short_url) is True
