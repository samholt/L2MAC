import url_shortener
from datetime import datetime, timedelta


def test_validate_url():
	assert url_shortener.validate_url('https://www.google.com') == True
	assert url_shortener.validate_url('https://www.nonexistentwebsite.com') == False


def test_generate_short_url():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 6
	assert url_shortener.DATABASE[url] == short_url


def test_custom_short_link():
	url = 'https://www.google.com'
	custom_link = 'custom'
	assert url_shortener.custom_short_link(url, custom_link) == custom_link
	assert url_shortener.DATABASE[url] == custom_link
	custom_link = 'custom'
	assert url_shortener.custom_short_link(url, custom_link) == 'Link already in use'


def test_set_expiration():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url)
	assert url_shortener.set_expiration(short_url, 10) == 'Expiration time set'
	assert short_url in url_shortener.EXPIRATION
	assert url_shortener.EXPIRATION[short_url] > datetime.now()
	assert url_shortener.set_expiration('nonexistent', 10) == 'Short URL not found'

