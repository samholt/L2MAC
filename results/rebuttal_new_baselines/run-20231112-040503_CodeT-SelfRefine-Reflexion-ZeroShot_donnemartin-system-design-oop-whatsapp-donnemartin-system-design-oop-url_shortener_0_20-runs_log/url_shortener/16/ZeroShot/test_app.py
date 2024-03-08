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
def url():
	return app.URL('http://example.com', '12345678', 'user1', [], datetime.now() + timedelta(days=1))

def test_shorten_url(client, url):
	response = client.post('/shorten', json={'url': url.original, 'user': url.user, 'expiration': url.expiration.isoformat()})
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()

def test_redirect_url(client, url):
	app.DB[url.shortened] = url
	response = client.get('/' + url.shortened)
	assert response.status_code == 302
	assert response.location == url.original

def test_redirect_url_not_found_or_expired(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert response.data == b'URL not found or expired'
