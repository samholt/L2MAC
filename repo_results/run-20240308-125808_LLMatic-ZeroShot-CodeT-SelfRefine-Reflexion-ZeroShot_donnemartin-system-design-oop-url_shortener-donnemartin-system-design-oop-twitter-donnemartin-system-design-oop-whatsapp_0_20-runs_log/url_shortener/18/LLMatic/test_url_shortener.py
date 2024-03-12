import url_shortener
from datetime import datetime, timedelta


def test_validate_url():
	assert url_shortener.validate_url('https://www.google.com') == True
	assert url_shortener.validate_url('invalid_url') == False


def test_generate_short_url():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 6
	assert url_shortener.DATABASE[url] == short_url
	assert url_shortener.EXPIRATION_TIMES[short_url] > datetime.now()


def test_custom_short_link():
	url = 'https://www.google.com'
	custom_link = 'custom'
	assert url_shortener.custom_short_link(url, custom_link) == custom_link
	assert url_shortener.custom_short_link(url, custom_link) == 'Error: Custom link already in use'
	assert url_shortener.EXPIRATION_TIMES[custom_link] > datetime.now()


def test_set_expiration_time():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url)
	new_expiration_time = url_shortener.set_expiration_time(short_url, 1)  # set expiration time to 1 day
	assert new_expiration_time == url_shortener.EXPIRATION_TIMES[short_url]


def test_get_original_url():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url)
	assert url_shortener.get_original_url(short_url) == url
	url_shortener.set_expiration_time(short_url, -1)  # set expiration time to 1 day ago
	assert url_shortener.get_original_url(short_url) == 'Error: This link has expired'

