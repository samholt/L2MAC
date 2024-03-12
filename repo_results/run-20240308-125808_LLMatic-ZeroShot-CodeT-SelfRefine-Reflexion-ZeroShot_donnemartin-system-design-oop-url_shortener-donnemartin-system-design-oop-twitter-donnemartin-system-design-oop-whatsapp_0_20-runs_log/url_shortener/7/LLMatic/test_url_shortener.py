import url_shortener
from datetime import datetime, timedelta


def test_generate_short_url():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 10
	assert short_url.isalnum()

	another_url = 'https://www.different.com'
	another_short_url = url_shortener.generate_short_url(another_url)
	assert another_short_url != short_url

	custom_short_link = 'custom'
	custom_url = url_shortener.generate_short_url(url, custom_short_link)
	assert custom_url == custom_short_link


def test_validate_url():
	valid_url = 'https://www.example.com'
	invalid_url = 'https://www.invalid.com'
	assert url_shortener.validate_url(valid_url)
	assert not url_shortener.validate_url(invalid_url)


def test_is_expired():
	url = 'https://www.example.com'
	short_url = url_shortener.generate_short_url(url, expiration_date=datetime.now() - timedelta(minutes=1))
	assert url_shortener.is_expired(short_url)

	short_url = url_shortener.generate_short_url(url, expiration_date=datetime.now() + timedelta(minutes=1))
	assert not url_shortener.is_expired(short_url)
