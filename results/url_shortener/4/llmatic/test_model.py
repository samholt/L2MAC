import pytest
import datetime
from model import URL, URLDatabase


def test_url_creation():
	url = URL('long_url', 'short_url')
	assert url.long_url == 'long_url'
	assert url.short_url == 'short_url'
	assert url.click_count == 0
	assert url.expiration_date > datetime.datetime.now()


def test_url_increment_click_count():
	url = URL('long_url', 'short_url')
	url.increment_click_count()
	assert url.click_count == 1


def test_url_database():
	db = URLDatabase()
	url = URL('long_url', 'short_url')
	db.add_url(url)
	retrieved_url = db.get_url('short_url')
	assert retrieved_url == url
	db.update_click_count('short_url')
	assert retrieved_url.click_count == 1
	db.delete_expired_urls()
	assert db.get_url('short_url') == url

