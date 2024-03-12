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
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

	response = client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'User already exists'

def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'

	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'wrong'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid username or password'

	response = client.post('/login', data=json.dumps({'username': 'wrong', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid username or password'

def test_shorten(client):
	response = client.post('/shorten', data=json.dumps({'original_url': 'https://www.google.com', 'short_url': 'google', 'username': 'test', 'expiration': '2022-12-31T23:59:59+0000'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'URL shortened successfully'

	response = client.post('/shorten', data=json.dumps({'original_url': 'https://www.google.com', 'short_url': 'google', 'username': 'test', 'expiration': '2022-12-31T23:59:59+0000'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Short URL already exists'

	response = client.get('/google')
	assert response.status_code == 302

	response = client.get('/wrong')
	assert response.status_code == 404
	assert response.get_json()['message'] == 'URL not found or expired'
