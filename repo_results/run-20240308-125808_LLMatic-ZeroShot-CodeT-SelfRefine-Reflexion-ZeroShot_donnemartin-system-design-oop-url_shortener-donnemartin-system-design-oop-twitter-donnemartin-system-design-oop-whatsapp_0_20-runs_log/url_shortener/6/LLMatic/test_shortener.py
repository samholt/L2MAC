import pytest
from shortener import Shortener
from datetime import datetime, timedelta


def test_generate_short_url():
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	assert len(short_url) == 6


def test_validate_url():
	shortener = Shortener()
	assert shortener.validate_url('https://www.google.com')
	assert not shortener.validate_url('invalid_url')


def test_get_original_url():
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	assert shortener.get_original_url(short_url) == 'https://www.google.com'


def test_record_click():
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	shortener.record_click(short_url, 'USA')
	assert shortener.get_clicks(short_url) == 1


def test_get_click_details():
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	shortener.record_click(short_url, 'USA')
	assert len(shortener.get_click_details(short_url)) == 1


def test_set_expiration():
	shortener = Shortener()
	short_url = shortener.generate_short_url('https://www.google.com')
	expiration_datetime = datetime.now() + timedelta(days=1)
	shortener.set_expiration(short_url, expiration_datetime)
	assert shortener.get_expiration(short_url) == expiration_datetime
