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

def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User created successfully.'}

	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Username already exists.'}

def test_create_url(client):
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'message' in data and data['message'] == 'URL created successfully.'
	assert 'short_url' in data

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'test', 'short_url': data['short_url']})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Short URL already exists.'}

	response = client.get('/' + data['short_url'])
	assert response.status_code == 302

	response = client.get('/analytics', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data[data.keys()[0]]['clicks'] == 1

	response = client.get('/analytics', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}

	response = client.get('/analytics', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}
