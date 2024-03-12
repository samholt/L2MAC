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
	assert response.status_code == 201
	assert 'shortened_url' in response.get_json()

def test_redirect_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com'}), content_type='application/json')
	short_url = response.get_json()['shortened_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

def test_create_user(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created'
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['error'] == 'User already exists'

def test_get_user(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.get('/user/test', data=json.dumps({'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['username'] == 'test'

def test_delete_user(client):
	client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.delete('/user/test', data=json.dumps({'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User deleted'
