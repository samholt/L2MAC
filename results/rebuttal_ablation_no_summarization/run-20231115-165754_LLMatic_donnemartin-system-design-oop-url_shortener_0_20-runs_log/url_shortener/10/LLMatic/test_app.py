import pytest
import app
import json
from datetime import datetime, timedelta
import time

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Username is already in use'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User logged in successfully'}
	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'error': 'Invalid username or password'}


def test_shorten_url(client):
	response = client.post('/', json={'username': 'test', 'url': 'https://www.google.com'})
	assert response.status_code == 201
	assert 'short_url' in json.loads(response.data)


def test_redirect_url(client):
	response = client.post('/', json={'username': 'test', 'url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/test/{short_url}')
	assert response.status_code == 302


def test_url_expiration(client):
	expiration = (datetime.now() + timedelta(seconds=1)).isoformat()
	response = client.post('/', json={'username': 'test', 'url': 'https://www.google.com', 'expiration': expiration})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/test/{short_url}')
	assert response.status_code == 302
	time.sleep(2)
	response = client.get(f'/test/{short_url}')
	assert response.status_code == 404
	assert json.loads(response.data) == {'error': 'URL has expired'}
