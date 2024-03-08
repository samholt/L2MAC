import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Username already exists'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password'}

	response = client.post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password'}

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com'})
	assert response.status_code == 200
	short_url = json.loads(response.data)['short_url']
	assert len(short_url) == 10

	response = client.get(f'/{short_url}')
	assert response.status_code == 302
	assert response.location == 'https://www.google.com'

	response = client.get('/wrong')
	assert response.status_code == 404
	assert json.loads(response.data) == {'message': 'URL not found or expired'}
