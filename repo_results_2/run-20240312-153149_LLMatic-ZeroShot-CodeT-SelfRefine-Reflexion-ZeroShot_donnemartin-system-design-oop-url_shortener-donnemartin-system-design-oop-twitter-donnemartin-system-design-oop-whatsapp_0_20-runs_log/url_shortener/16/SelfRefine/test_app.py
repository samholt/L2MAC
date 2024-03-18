import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'http://example.com'})
	assert response.status_code == 200
	assert 'short_url' in json.loads(response.data)


def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'http://example.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	response = client.post('/shorten', json={'url': 'http://example.com', 'username': 'test'})
	assert response.status_code == 200
	response = client.get('/analytics?username=test')
	assert response.status_code == 200
	assert len(json.loads(response.data)) == 1


def test_register_user(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'message' in json.loads(response.data)
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert 'error' in json.loads(response.data)


def test_admin_dashboard(client):
	response = client.get('/admin')
	assert response.status_code == 200
	assert len(json.loads(response.data)) > 0
