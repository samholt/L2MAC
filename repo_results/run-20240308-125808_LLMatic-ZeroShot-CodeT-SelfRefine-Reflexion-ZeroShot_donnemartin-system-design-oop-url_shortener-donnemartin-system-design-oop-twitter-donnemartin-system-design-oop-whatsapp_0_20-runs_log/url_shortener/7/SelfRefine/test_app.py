import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	client.post('/users', json={'username': 'test', 'password': 'password'})
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test', 'expiration': '2022-12-31 23:59:59'})
	assert response.status_code == 201
	assert 'short_url' in json.loads(response.data)


def test_redirect_url(client):
	client.post('/users', json={'username': 'test', 'password': 'password'})
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test', 'expiration': '2022-12-31 23:59:59'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	client.post('/users', json={'username': 'test', 'password': 'password'})
	response = client.get('/analytics?username=test')
	assert response.status_code == 200
	assert isinstance(json.loads(response.data), list)


def test_create_user(client):
	response = client.post('/users', json={'username': 'test', 'password': 'password'})
	assert response.status_code == 201
	assert 'message' in json.loads(response.data)


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert isinstance(json.loads(response.data), list)
