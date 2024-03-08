import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'short_url' in data


def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user'})
	data = json.loads(response.data)
	short_url = data['short_url']

	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'user': 'test_user'})
	data = json.loads(response.data)
	short_url = data['short_url']

	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'clicks' in data
