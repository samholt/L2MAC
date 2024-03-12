import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'long_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in json.loads(response.data)


def test_redirect_to_long_url(client):
	response = client.post('/shorten_url', json={'long_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'


def test_redirect_to_long_url_not_found(client):
	response = client.get('/random_url')
	assert response.status_code == 404
