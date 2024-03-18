import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Test URL shortening

def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'short': 'ggl'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == {'short_url': 'ggl'}

# Test URL redirection

def test_redirect_url(client):
	response = client.get('/ggl')
	assert response.status_code == 302

# Test user creation

def test_create_user(client):
	response = client.post('/user', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User created successfully'}

# Test get user

def test_get_user(client):
	response = client.get('/user/test')
	assert response.status_code == 200
	assert 'urls' in json.loads(response.data)
