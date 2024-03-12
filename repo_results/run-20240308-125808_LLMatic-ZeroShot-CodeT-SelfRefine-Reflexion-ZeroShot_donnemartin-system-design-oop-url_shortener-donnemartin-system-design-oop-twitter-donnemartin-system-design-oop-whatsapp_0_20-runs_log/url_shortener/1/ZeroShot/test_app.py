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
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	short_url = response.get_json()['short_url']

	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'expiration': '2022-12-31 23:59:59'}), content_type='application/json')
	short_url = response.get_json()['short_url']

	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()
