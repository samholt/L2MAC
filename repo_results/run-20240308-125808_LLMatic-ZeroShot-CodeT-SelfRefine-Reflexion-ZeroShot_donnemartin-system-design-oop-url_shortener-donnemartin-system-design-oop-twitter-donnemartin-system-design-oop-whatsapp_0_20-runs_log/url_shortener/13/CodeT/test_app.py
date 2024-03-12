import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	# Reset mock database after each test
		app.urls = {}
		app.users = {}

def test_shorten_url(client):
	# Test URL shortening
	response = client.post('/shorten', json={'url': 'http://example.com'})
	assert response.status_code == 200
	assert 'short_url' in json.loads(response.data)

	# Test custom short URL
	response = client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	assert response.status_code == 200
	assert json.loads(response.data)['short_url'] == 'custom'

	# Test custom short URL already in use
	response = client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	assert response.status_code == 400

	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid'})
	assert response.status_code == 400

def test_redirect_to_original(client):
	# Test redirect to original URL
	client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	response = client.get('/custom')
	assert response.status_code == 302
	assert response.location == 'http://example.com'

	# Test URL not found
	response = client.get('/notfound')
	assert response.status_code == 404

def test_get_analytics(client):
	# Test get analytics
	client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	client.get('/custom')
	response = client.get('/analytics')
	assert response.status_code == 200
	assert json.loads(response.data)['urls'][0]['clicks'] == 1

def test_create_user(client):
	# Test create user
	response = client.post('/users', json={'username': 'user', 'password': 'pass'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User created successfully'

	# Test username already in use
	response = client.post('/users', json={'username': 'user', 'password': 'pass'})
	assert response.status_code == 400

def test_get_user(client):
	# Test get user
	client.post('/users', json={'username': 'user', 'password': 'pass'})
	response = client.get('/users/user')
	assert response.status_code == 200
	assert json.loads(response.data)['username'] == 'user'

	# Test user not found
	response = client.get('/users/notfound')
	assert response.status_code == 404
