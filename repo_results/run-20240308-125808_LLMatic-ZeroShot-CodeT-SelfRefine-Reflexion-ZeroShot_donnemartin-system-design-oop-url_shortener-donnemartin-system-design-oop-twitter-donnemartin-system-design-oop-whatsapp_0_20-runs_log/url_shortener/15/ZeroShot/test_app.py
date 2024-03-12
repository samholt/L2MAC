import pytest
import app
import json
from flask import Flask
from werkzeug.wrappers import response

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
	response = client.post('/shorten', json={'username': 'test', 'url': 'https://www.google.com'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'message' in data
	assert 'short_url' in data
	assert data['message'] == 'URL shortened successfully'


def test_redirect(client):
	response = client.post('/shorten', json={'username': 'test', 'url': 'https://www.google.com'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_analytics(client):
	response = client.get('/analytics', json={'username': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert isinstance(data, dict)
