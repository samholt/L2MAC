import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_shorten(client):
	response = client.post('/shorten', json={'username': 'test', 'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'message' in data and data['message'] == 'URL shortened successfully'
	assert 'short_url' in data


def test_redirect_to_original(client):
	response = client.post('/shorten', json={'username': 'test', 'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_expired_url(client):
	response = client.post('/shorten', json={'username': 'test', 'original_url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	app.urls[short_url].expiration = datetime.now() - timedelta(days=1) # Set URL to be expired
	response = client.get(f'/{short_url}')
	assert response.status_code == 404


def test_already_shortened_url(client):
	response = client.post('/shorten', json={'username': 'test', 'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	response = client.post('/shorten', json={'username': 'test', 'original_url': 'https://www.google.com'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'message' in data and data['message'] == 'URL already shortened'


def test_shorten_without_login(client):
	response = client.post('/shorten', json={'username': 'test2', 'original_url': 'https://www.google.com'})
	assert response.status_code == 404
	data = json.loads(response.data)
	assert 'message' in data and data['message'] == 'User not found'


def test_analytics(client):
	response = client.get('/analytics', json={'username': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert isinstance(data, dict)
