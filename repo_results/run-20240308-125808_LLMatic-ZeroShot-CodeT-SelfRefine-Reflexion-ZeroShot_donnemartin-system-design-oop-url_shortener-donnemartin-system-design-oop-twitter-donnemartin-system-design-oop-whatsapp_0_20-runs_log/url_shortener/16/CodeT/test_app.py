import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}

	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Username already exists'}

def test_create_url(client):
	response = client.post('/create_url', json={'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert data['message'] == 'URL created successfully'
	assert 'short_url' in data

	response = client.post('/create_url', json={'username': 'test', 'password': 'test', 'original_url': 'https://www.google.com', 'short_url': data['short_url']})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Short URL already exists'}

	response = client.post('/create_url', json={'username': 'test', 'password': 'test', 'original_url': 'invalid_url'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid URL'}

	response = client.post('/create_url', json={'username': 'invalid', 'password': 'invalid', 'original_url': 'https://www.google.com'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid credentials'}

	response = client.get('/' + data['short_url'])
	assert response.status_code == 302

	response = client.get('/analytics', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert len(data) == 1
	assert 'clicks' in data.values()[0]
	assert 'last_clicked' in data.values()[0]
