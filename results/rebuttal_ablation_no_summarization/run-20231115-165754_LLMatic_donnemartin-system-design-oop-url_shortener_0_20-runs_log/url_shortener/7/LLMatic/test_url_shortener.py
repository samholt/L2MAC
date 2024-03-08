import pytest
from url_shortener import generate_short_url, handle_custom_short_link, DATABASE
from datetime import datetime, timedelta


def test_generate_short_url():
	url = 'https://www.google.com'
	short_url = generate_short_url(url)
	assert short_url in DATABASE
	assert DATABASE[short_url]['url'] == url
	assert DATABASE[short_url]['expiry_date'] > datetime.now()


def test_handle_custom_short_link():
	url = 'https://www.google.com'
	custom_link = 'custom'
	short_url = handle_custom_short_link(url, custom_link)
	assert short_url == custom_link
	assert DATABASE[short_url]['url'] == url
	assert DATABASE[short_url]['expiry_date'] > datetime.now()


def test_expired_url():
	url = 'https://www.google.com'
	short_url = generate_short_url(url, expiry_days=-1)
	assert DATABASE[short_url]['expiry_date'] < datetime.now()
