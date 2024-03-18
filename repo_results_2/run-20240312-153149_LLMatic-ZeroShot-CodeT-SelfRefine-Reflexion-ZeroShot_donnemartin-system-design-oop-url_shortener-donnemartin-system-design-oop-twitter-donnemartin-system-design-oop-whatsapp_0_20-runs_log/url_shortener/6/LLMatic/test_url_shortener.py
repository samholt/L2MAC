import url_shortener
from datetime import datetime, timedelta

def test_generate_short_url():
	short_url = url_shortener.generate_short_url()
	assert len(short_url) == 6
	assert short_url.isalnum()


def test_validate_url():
	assert url_shortener.validate_url('https://www.google.com')
	assert not url_shortener.validate_url('https://www.nonexistentwebsite123456.com')


def test_set_url_expiration():
	short_url = url_shortener.generate_short_url()
	url_shortener.set_url_expiration(short_url, 1)
	assert url_shortener.url_db[short_url]['expiration'] > datetime.now()


def test_check_url_expiration():
	short_url = url_shortener.generate_short_url()
	url_shortener.set_url_expiration(short_url, -1)
	assert url_shortener.check_url_expiration(short_url)
