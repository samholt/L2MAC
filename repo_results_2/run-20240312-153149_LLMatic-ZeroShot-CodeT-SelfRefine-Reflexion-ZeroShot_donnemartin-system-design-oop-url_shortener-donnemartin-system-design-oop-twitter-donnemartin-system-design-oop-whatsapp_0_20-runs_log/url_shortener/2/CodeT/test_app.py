import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	app.DB = {}


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user', 'expiration': '2022-12-31T23:59:59'})
	assert response.status_code == 200
	assert 'shortened_url' in json.loads(response.data)


def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user', 'expiration': '2022-12-31T23:59:59'})
	short_url = json.loads(response.data)['shortened_url']

	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user', 'expiration': '2022-12-31T23:59:59'})
	response = client.get('/analytics?user=test_user')
	assert response.status_code == 200
	assert len(json.loads(response.data)['urls']) == 1


def test_get_admin(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert len(json.loads(response.data)['urls']) == 0
