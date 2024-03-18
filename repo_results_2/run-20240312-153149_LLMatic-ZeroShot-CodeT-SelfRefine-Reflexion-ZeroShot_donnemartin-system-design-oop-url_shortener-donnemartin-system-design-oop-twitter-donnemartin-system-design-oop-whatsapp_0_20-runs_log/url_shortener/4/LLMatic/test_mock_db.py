import pytest
from mock_db import MockDB

@pytest.fixture
def db():
	return MockDB()


def test_add_url(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.add_url('https://www.google.com', 'google', 'test') is None
	assert db.add_url('https://www.google.com', None, 'test') == '1'


def test_get_url(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.get_url('google') == 'https://www.google.com'
	assert db.get_url('ggl') is None


def test_get_analytics(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.get_analytics('google') == {'clicks': 0, 'timestamps': []}
	assert db.get_analytics('ggl') is None


def test_get_user_analytics(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.get_user_analytics('test') == {'google': {'clicks': 0, 'timestamps': []}}
	assert db.get_user_analytics('test2') is None


def test_create_account(db):
	assert db.create_account('test', 'test') == 'Account created'


def test_get_user_urls(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.get_user_urls('test') == {'google': 'https://www.google.com'}
	assert db.get_user_urls('test2') == {}


def test_update_url(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.update_url('test', 'google', 'ggl') == 'URL updated'
	assert db.update_url('test', 'google', 'ggl') == 'URL not found'


def test_delete_url(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.delete_url('test', 'google') == 'URL deleted'
	assert db.delete_url('test', 'google') == 'URL not found'


def test_delete_admin(db):
	db.add_url('https://www.google.com', 'google', 'test')
	assert db.delete_admin('test', 'google') == 'URL deleted'
	assert db.delete_admin('test', 'google') == 'URL not found'
	assert db.delete_admin('test', None) == 'Account deleted'
	assert db.delete_admin('test', None) == 'Account not found'

