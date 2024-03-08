import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert data['message'] == 'URL shortened successfully'
	assert 'short_url' in data


def test_redirect_to_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.get('/analytics')
	assert response.status_code == 200


def test_delete_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.delete('/delete_url', json={'short_url': short_url})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL deleted successfully'}
