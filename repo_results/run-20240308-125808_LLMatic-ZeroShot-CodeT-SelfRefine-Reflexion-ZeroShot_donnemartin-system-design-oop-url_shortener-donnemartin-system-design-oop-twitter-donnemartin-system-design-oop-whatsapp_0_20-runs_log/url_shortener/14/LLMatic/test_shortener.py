import shortener
from datetime import datetime, timedelta


def test_shorten_url():
	url_shortener = shortener.Shortener()
	original_url = 'http://long.url.com'
	short_url = url_shortener.shorten_url(original_url)
	assert 'http://short.url/' in short_url
	assert len(short_url) == 23
	short_url2 = url_shortener.shorten_url(original_url)
	assert short_url != short_url2


def test_validate_url():
	url_shortener = shortener.Shortener()
	assert url_shortener.validate_url('http://google.com')
	assert not url_shortener.validate_url('http://invalid.url')


def test_set_expiration():
	url_shortener = shortener.Shortener()
	original_url = 'http://long.url.com'
	short_url = url_shortener.shorten_url(original_url)
	expiration_datetime = datetime.now() + timedelta(minutes=1)
	assert url_shortener.set_expiration(short_url, expiration_datetime)
	assert url_shortener.get_url(short_url) == original_url
	expiration_datetime = datetime.now() - timedelta(minutes=1)
	url_shortener.set_expiration(short_url, expiration_datetime)
	assert url_shortener.get_url(short_url) == None
