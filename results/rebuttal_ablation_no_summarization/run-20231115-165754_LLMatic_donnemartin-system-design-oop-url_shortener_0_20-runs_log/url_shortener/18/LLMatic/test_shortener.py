import pytest
from shortener import Shortener


def test_shorten_url():
	short = Shortener()
	short_url = short.shorten_url('https://www.google.com')
	assert len(short_url) == 6


def test_validate_url():
	short = Shortener()
	assert short.validate_url('https://www.google.com') is True
	assert short.validate_url('invalid_url') is False


def test_get_original_url():
	short = Shortener()
	short_url = short.shorten_url('https://www.google.com')
	assert short.get_original_url(short_url) == 'https://www.google.com'


def test_track_click():
	short = Shortener()
	short_url = short.shorten_url('https://www.google.com')
	short.track_click(short_url, 'USA')
	click_data = short.get_click_data(short_url)
	assert click_data['clicks'] == 1
	assert click_data['click_data'][0]['location'] == 'USA'


def test_set_expiration():
	short = Shortener()
	short_url = short.shorten_url('https://www.google.com')
	short.set_expiration(short_url, '2022-12-31T23:59:59')
	assert short.get_original_url(short_url) is None

