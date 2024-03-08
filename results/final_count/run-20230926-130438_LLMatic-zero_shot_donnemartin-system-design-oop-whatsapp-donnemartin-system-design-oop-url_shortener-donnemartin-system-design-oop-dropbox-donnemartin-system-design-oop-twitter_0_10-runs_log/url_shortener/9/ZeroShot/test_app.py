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
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User created successfully.'}

	response = client.post('/create_user', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Username already exists.'}

def test_create_url(client):
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['message'] == 'URL created successfully.'
	assert 'short_url' in data

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'test', 'short_url': data['short_url']})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Short URL already exists.'}

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'test', 'short_url': 'custom'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL created successfully.', 'short_url': 'custom'}

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'test', 'short_url': 'custom'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Short URL already exists.'}

	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'username': 'test', 'password': 'test', 'expiration': '2022-12-31T23:59:59.999Z'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['message'] == 'URL created successfully.'
	assert 'short_url' in data

	response = client.get('/' + data['short_url'])
	assert response.status_code == 410
	assert json.loads(response.data) == {'message': 'URL has expired.'}

	response = client.get('/' + 'custom')
	assert response.status_code == 302

	response = client.get('/' + 'nonexistent')
	assert response.status_code == 404
	assert json.loads(response.data) == {'message': 'URL not found.'}

	response = client.post('/analytics', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'custom' in data
	assert data['custom']['clicks'] == 1
	assert len(data['custom']['click_data']) == 1

	response = client.post('/analytics', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}

	response = client.post('/analytics', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password.'}
