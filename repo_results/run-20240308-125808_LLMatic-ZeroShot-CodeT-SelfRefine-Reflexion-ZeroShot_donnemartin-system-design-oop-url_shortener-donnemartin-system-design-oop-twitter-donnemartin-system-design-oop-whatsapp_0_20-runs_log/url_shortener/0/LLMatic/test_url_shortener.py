import url_shortener
from datetime import datetime, timedelta
import time


def test_validate_url():
	assert url_shortener.validate_url('https://www.google.com') == True
	assert url_shortener.validate_url('invalid_url') == False


def test_generate_short_url():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 6
	assert url_shortener.DATABASE[short_url] == url


def test_custom_short_link():
	url = 'https://www.google.com'
	custom_link = 'google'
	assert url_shortener.custom_short_link(url, custom_link) == custom_link
	assert url_shortener.DATABASE[custom_link] == url
	assert url_shortener.custom_short_link(url, custom_link) == 'Custom link already in use'


def test_url_expiration():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url, 1)
	assert url_shortener.get_original_url(short_url) == url
	# Wait for the url to expire
	time.sleep(61)
	assert url_shortener.get_original_url(short_url) == None
