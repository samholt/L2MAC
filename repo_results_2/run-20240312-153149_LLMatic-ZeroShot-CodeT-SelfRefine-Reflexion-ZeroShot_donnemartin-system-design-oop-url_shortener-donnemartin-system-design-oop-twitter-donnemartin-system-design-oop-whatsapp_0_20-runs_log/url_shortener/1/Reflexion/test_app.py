import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def reset_db():
	app.DB = {}

@pytest.mark.parametrize('url, expiration', [
	('http://example.com', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://google.com', (datetime.now() + timedelta(hours=1)).isoformat()),
	('http://facebook.com', (datetime.now() - timedelta(days=1)).isoformat())
])
def test_shorten_url(client, reset_db, url, expiration):
	response = client.post('/shorten', data=json.dumps({'url': url, 'expiration': expiration}), content_type='application/json')
	assert response.status_code == 201
	short_url = response.get_json()['shortened_url']
	assert short_url in app.DB
	assert app.DB[short_url].original == url
	assert app.DB[short_url].expiration.isoformat() == expiration

@pytest.mark.parametrize('url, expiration', [
	('http://example.com', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://google.com', (datetime.now() - timedelta(hours=1)).isoformat()),
	('http://facebook.com', (datetime.now() - timedelta(days=1)).isoformat())
])
def test_redirect_to_url(client, reset_db, url, expiration):
	response = client.post('/shorten', data=json.dumps({'url': url, 'expiration': expiration}), content_type='application/json')
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	if datetime.fromisoformat(expiration) > datetime.now():
		assert response.status_code == 302
		assert response.location == url
	else:
		assert response.status_code == 404
