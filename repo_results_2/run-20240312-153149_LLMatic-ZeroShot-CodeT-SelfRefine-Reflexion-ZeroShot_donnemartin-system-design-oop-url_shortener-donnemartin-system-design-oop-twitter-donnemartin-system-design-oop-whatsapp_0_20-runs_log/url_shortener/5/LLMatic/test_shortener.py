import pytest
from shortener import Shortener
from datetime import datetime, timedelta


def test_generate_short_url():
	shortener = Shortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	assert len(short_url) == 6
	assert shortener.url_map[url] == short_url
	assert shortener.analytics[short_url] == {'clicks': 0, 'timestamps': [], 'locations': []}


def test_custom_short_url():
	shortener = Shortener()
	url = 'https://www.google.com'
	custom = 'google'
	short_url = shortener.custom_short_url(url, custom)
	assert short_url == custom
	assert shortener.url_map[url] == custom
	assert shortener.analytics[custom] == {'clicks': 0, 'timestamps': [], 'locations': []}


def test_get_original_url():
	shortener = Shortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	ip_address = '8.8.8.8'
	assert shortener.get_original_url(short_url, ip_address) == url
	assert shortener.analytics[short_url]['clicks'] == 1
	assert isinstance(shortener.analytics[short_url]['timestamps'][0], datetime)
	assert isinstance(shortener.analytics[short_url]['locations'][0], str)


def test_get_analytics():
	shortener = Shortener()
	url = 'https://www.google.com'
	short_url = shortener.generate_short_url(url)
	ip_address = '8.8.8.8'
	shortener.get_original_url(short_url, ip_address)
	analytics = shortener.get_analytics(short_url)
	assert analytics['clicks'] == 1
	assert isinstance(analytics['timestamps'][0], datetime)
	assert isinstance(analytics['locations'][0], str)


def test_url_expiration():
	shortener = Shortener()
	url = 'https://www.google.com'
	expiration = datetime.now() + timedelta(seconds=1)
	short_url = shortener.generate_short_url(url, expiration)
	ip_address = '8.8.8.8'
	assert shortener.get_original_url(short_url, ip_address) == url
	from time import sleep
	sleep(2)
	assert shortener.get_original_url(short_url, ip_address) == 'URL has expired'
