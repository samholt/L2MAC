import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Test user creation

def test_create_user(client):
	response = client.post('/users', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created'}

# Test URL shortening

def test_shorten_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test', 'expiration': '2022-12-31 23:59:59'})
	assert response.status_code == 201
	short_url = json.loads(response.data)['short_url']
	assert len(short_url) == 5

# Test URL redirection

def test_redirect_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test', 'expiration': '2022-12-31 23:59:59'})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302

# Test analytics

def test_get_analytics(client):
	response = client.get('/analytics?username=test')
	assert response.status_code == 200

# Test user URLs

def test_get_user_urls(client):
	response = client.get('/users/test/urls')
	assert response.status_code == 200

# Test admin URLs

def test_get_all_urls(client):
	response = client.get('/admin/urls')
	assert response.status_code == 200

# Test admin users

def test_get_all_users(client):
	response = client.get('/admin/users')
	assert response.status_code == 200

# Test user deletion

def test_delete_user(client):
	response = client.delete('/admin/users/test')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User deleted'}

# Test URL deletion

def test_delete_url(client):
	response = client.post('/shorten', json={'url': 'https://www.google.com', 'username': 'test', 'expiration': '2022-12-31 23:59:59'})
	short_url = json.loads(response.data)['short_url']
	response = client.delete(f'/admin/urls/{short_url}')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'URL deleted'}
