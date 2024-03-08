import pytest
from utils import validate_url, shorten_url, record_click, click_db


def test_validate_url():
	assert validate_url('https://www.google.com')
	assert not validate_url('invalid_url')


def test_shorten_url():
	url = 'https://www.google.com'
	short_url = shorten_url(url)
	assert short_url.startswith('http://short.ly/')
	assert len(short_url) == 24


def test_record_click():
	short_url = 'http://short.ly/test'
	original_url = 'http://example.com'
	location = 'Unknown'
	click = record_click(short_url, original_url, location)
	assert click in click_db[short_url]
	assert click.url.original_url == original_url
	assert click.url.shortened_url == short_url
	assert click.location == location
