import pytest
import app
from flask import Flask
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def setup_db():
	app.DB = {}
	url = app.URL('https://www.google.com', 'google', 'test_user', [], datetime.now() + timedelta(days=1))
	app.DB['google'] = url

	url = app.URL('https://www.facebook.com', 'fb', 'test_user', [], datetime.now() - timedelta(days=1))
	app.DB['fb'] = url

	yield

	app.DB = {}


def test_shorten_url(client, setup_db):
	response = client.post('/shorten', json={'url': 'https://www.twitter.com', 'shortened': 'twitter', 'user': 'test_user', 'expiration': (datetime.now() + timedelta(days=1)).isoformat()})
	assert response.status_code == 200
	assert 'message' in response.get_json()
	assert response.get_json()['message'] == 'URL shortened successfully'


def test_redirect_url(client, setup_db):
	response = client.get('/google')
	assert response.status_code == 302


def test_expired_url(client, setup_db):
	response = client.get('/fb')
	assert response.status_code == 400
	assert 'error' in response.get_json()
	assert response.get_json()['error'] == 'URL has expired'


def test_get_analytics(client, setup_db):
	response = client.get('/analytics?user=test_user')
	assert response.status_code == 200
	assert 'urls' in response.get_json()
	assert len(response.get_json()['urls']) == 2
