import url_shortener
from datetime import datetime, timedelta


def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert isinstance(short_url, str)

	custom_short_link = 'custom'
	custom_url = url_shortener.generate_short_url(url, custom_short_link)
	assert custom_url == custom_short_link


def test_validate_url():
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalidurl.com'
	assert url_shortener.validate_url(valid_url) is True
	assert url_shortener.validate_url(invalid_url) is False


def test_expiration():
	valid_url = 'https://www.example.com'

	# Generate a short URL with an expiration time in the future
	future_time = datetime.now() + timedelta(minutes=1)
	short_url = url_shortener.generate_short_url(valid_url, expiration_time=future_time)
	assert url_shortener.validate_url(short_url) is True

	# Generate a short URL with an expiration time in the past
	past_time = datetime.now() - timedelta(minutes=1)
	short_url = url_shortener.generate_short_url(valid_url, expiration_time=past_time)
	assert url_shortener.validate_url(short_url) is False
