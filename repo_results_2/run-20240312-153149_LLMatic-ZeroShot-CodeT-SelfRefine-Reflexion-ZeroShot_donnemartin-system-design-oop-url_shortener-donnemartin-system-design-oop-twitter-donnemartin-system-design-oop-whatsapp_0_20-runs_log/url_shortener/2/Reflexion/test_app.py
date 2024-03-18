import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_url(client):
	response = client.post('/', json={'url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/', json={'url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'


def test_redirect_url_not_found(client):
	response = client.get('/nonexistent')
	assert response.status_code == 404
