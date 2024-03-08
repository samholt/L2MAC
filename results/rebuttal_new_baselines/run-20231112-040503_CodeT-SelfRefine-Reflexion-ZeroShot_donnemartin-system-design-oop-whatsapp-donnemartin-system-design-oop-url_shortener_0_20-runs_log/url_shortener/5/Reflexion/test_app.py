import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'shortened_url' in response.get_json()

def test_redirect_to_original(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	shortened_url = response.get_json()['shortened_url']
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302

def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

def test_login(client):
	client.post('/register', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Login successful'
