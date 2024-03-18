import pytest
from shortener import Shortener
from models import URL
from datetime import datetime, timedelta


def test_shorten_url():
	shortener = Shortener()
	url = 'http://example.com'
	short_url = shortener.shorten_url(url, 'admin')
	assert short_url in shortener.urls
	assert shortener.urls[short_url].original_url == url


def test_record_click():
	shortener = Shortener()
	short_url = 'test'
	location = 'test_location'
	shortener.record_click(short_url, location)
	assert shortener.clicks[0].short_url == short_url
	assert shortener.clicks[0].location == location


def test_get_clicks():
	shortener = Shortener()
	short_url = 'test'
	location = 'test_location'
	shortener.record_click(short_url, location)
	clicks = shortener.get_clicks(short_url)
	assert len(clicks) == 1
	assert clicks[0].short_url == short_url
	assert clicks[0].location == location
