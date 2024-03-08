import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'original_url': 'https://google.com', 'user_id': '123'})
	assert response.status_code == 201
	assert 'short_url' in json.loads(response.data)


def test_redirect_url(client):
	response = client.post('/shorten', json={'original_url': 'https://google.com', 'user_id': '123'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', json={'original_url': 'https://google.com', 'user_id': '123'})
	response = client.get('/analytics?user_id=123')
	assert response.status_code == 200
	assert 'urls' in json.loads(response.data)
