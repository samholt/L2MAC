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
def reset_db():
	app.DB = {}

@pytest.mark.parametrize('url', [
	'http://example.com',
	'https://example.com',
	'http://www.example.com',
	'https://www.example.com'
])
def test_shorten_url(client, reset_db, url):
	response = client.post('/shorten', json={'url': url})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()

@pytest.mark.parametrize('url', [
	'example.com',
	'http://',
	'https://',
	'http://www.',
	'https://www.'
])
def test_shorten_invalid_url(client, reset_db, url):
	response = client.post('/shorten', json={'url': url})
	assert response.status_code == 400
	assert 'error' in response.get_json()

@pytest.mark.parametrize('url', [
	'http://example.com',
	'https://example.com',
	'http://www.example.com',
	'https://www.example.com'
])
def test_redirect_to_url(client, reset_db, url):
	response = client.post('/shorten', json={'url': url})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

@pytest.mark.parametrize('url', [
	'http://example.com',
	'https://example.com',
	'http://www.example.com',
	'https://www.example.com'
])
def test_redirect_to_expired_url(client, reset_db, url):
	response = client.post('/shorten', json={'url': url, 'expires_at': (datetime.now() - timedelta(days=1)).isoformat()})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 400
	assert 'error' in response.get_json()
