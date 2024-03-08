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

@pytest.mark.parametrize('url, shortened, expires_at', [
	('http://example.com', 'exmpl', (datetime.now() + timedelta(days=1)).isoformat()),
	('http://google.com', 'goog', (datetime.now() + timedelta(days=1)).isoformat()),
])
def test_shorten_url(client, reset_db, url, shortened, expires_at):
	response = client.post('/shorten', data=json.dumps({'url': url, 'shortened': shortened, 'expires_at': expires_at}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'shortened_url': shortened}

@pytest.mark.parametrize('shortened, url', [
	('exmpl', 'http://example.com'),
	('goog', 'http://google.com'),
])
def test_redirect_to_url(client, reset_db, shortened, url):
	expires_at = (datetime.now() + timedelta(days=1)).isoformat()
	client.post('/shorten', data=json.dumps({'url': url, 'shortened': shortened, 'expires_at': expires_at}), content_type='application/json')
	response = client.get(f'/{shortened}')
	assert response.status_code == 302
	assert response.location == url
