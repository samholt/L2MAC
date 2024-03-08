import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}

def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'username': 'test', 'original_url': 'https://www.google.com', 'short_url': 'goog', 'expiration_date': '2022-12-31T23:59:59Z'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'URL shortened successfully'}

def test_redirect_url(client):
	response = client.get('/goog')
	assert response.status_code == 302
	assert response.headers['Location'] == 'https://www.google.com'

def test_expired_url(client):
	response = client.get('/expired')
	assert response.status_code == 404
	assert response.get_json() == {'message': 'URL not found or expired'}
