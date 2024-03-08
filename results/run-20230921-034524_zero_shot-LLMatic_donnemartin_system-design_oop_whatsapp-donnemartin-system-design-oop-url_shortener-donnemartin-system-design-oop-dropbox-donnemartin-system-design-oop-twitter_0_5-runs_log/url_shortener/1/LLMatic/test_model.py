import datetime
import pytest
from model import URL, URLStore


def test_url():
	url = URL('http://example.com')
	assert len(url.short_url) == 6
	assert url.clicks == 0
	assert url.is_expired() == False

	url.increment_clicks()
	assert url.clicks == 1

	url = URL('http://example.com', datetime.datetime.now() + datetime.timedelta(days=1))
	assert url.is_expired() == False


def test_url_store():
	store = URLStore()
	url = URL('http://example.com')
	store.add_url(url)
	assert store.get_url(url.short_url) == url

	store.delete_expired_urls()
	assert store.get_url(url.short_url) == url

	url = URL('http://example.com', datetime.datetime.now() - datetime.timedelta(days=1))
	store.add_url(url)
	store.delete_expired_urls()
	assert store.get_url(url.short_url) == None

