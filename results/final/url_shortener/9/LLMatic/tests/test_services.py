import services
import pytest
from datetime import datetime, timedelta


def test_generate_short_url():
	short_url = services.generate_short_url('https://www.google.com')
	assert len(short_url) == 5


def test_validate_and_shorten_url():
	short_url = services.validate_and_shorten_url('https://www.google.com')
	assert short_url is not None


def test_get_original_url():
	short_url = services.validate_and_shorten_url('https://www.google.com')
	original_url = services.get_original_url(short_url)
	assert original_url == 'https://www.google.com'


def test_get_expired_url():
	short_url = services.validate_and_shorten_url('https://www.google.com', expiration=datetime.now() - timedelta(days=1))
	original_url = services.get_original_url(short_url)
	assert original_url is None


def test_record_click():
	short_url = services.validate_and_shorten_url('https://www.google.com')
	click_count = services.record_click(short_url, '127.0.0.1')
	assert click_count == 1


def test_create_user():
	message = services.create_user('test', 'test')
	assert message == 'User created successfully'


def test_authenticate_user():
	services.create_user('test', 'test')
	is_authenticated = services.authenticate_user('test', 'test')
	assert is_authenticated


def test_get_user_urls():
	services.create_user('test', 'test')
	short_url = services.validate_and_shorten_url('https://www.google.com', 'test')
	urls = services.get_user_urls('test')
	assert urls == {short_url: 'https://www.google.com'}


def test_get_all_urls():
	short_url = services.validate_and_shorten_url('https://www.google.com')
	urls = services.get_all_urls()
	assert short_url in urls


def test_delete_url():
	short_url = services.validate_and_shorten_url('https://www.google.com')
	message = services.delete_url(short_url)
	assert message == 'URL deleted successfully'


def test_get_all_users():
	services.create_user('test', 'test')
	users = services.get_all_users()
	assert 'test' in users


def test_delete_user():
	services.create_user('test', 'test')
	message = services.delete_user('test')
	assert message == 'User deleted successfully'
