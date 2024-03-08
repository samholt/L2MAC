import datetime
import pytest
from model import URL, URLStore


def test_url_generation():
	url = URL('https://www.example.com')
	assert len(url.short_url) == 6
	assert url.clicks == 0
	assert url.is_expired() == False


def test_url_expiry():
	expiry_date = datetime.datetime.now() - datetime.timedelta(days=1)
	url = URL('https://www.example.com', expiry_date)
	assert url.is_expired() == True


def test_url_store():
	store = URLStore()
	url = URL('https://www.example.com')
	store.add_url(url)
	assert store.get_url(url.short_url) == url
	store.delete_expired_urls()
	assert store.get_url(url.short_url) == url

