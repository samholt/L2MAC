import url_shortener
from datetime import datetime, timedelta


def test_validate_url():
	assert url_shortener.validate_url('https://www.google.com')
	assert not url_shortener.validate_url('https://www.nonexistentwebsite.com')


def test_generate_short_url():
	url = 'https://www.google.com'
	short_url = url_shortener.generate_short_url(url)
	assert len(short_url) == 6


def test_handle_custom_short_link():
	url_database = {}
	custom_link = 'custom'
	assert url_shortener.handle_custom_short_link(custom_link, url_database)
	assert not url_shortener.handle_custom_short_link(custom_link, url_database)


def test_set_expiration():
	url_database = {'test': {'url': 'https://www.google.com', 'expiration': None}}
	assert url_shortener.set_expiration('test', url_database, 10)
	assert url_database['test']['expiration'] is not None


def test_is_expired():
	url_database = {'test': {'url': 'https://www.google.com', 'expiration': datetime.now() - timedelta(minutes=1)}}
	assert url_shortener.is_expired('test', url_database)
	url_database = {'test': {'url': 'https://www.google.com', 'expiration': datetime.now() + timedelta(minutes=1)}}
	assert not url_shortener.is_expired('test', url_database)
