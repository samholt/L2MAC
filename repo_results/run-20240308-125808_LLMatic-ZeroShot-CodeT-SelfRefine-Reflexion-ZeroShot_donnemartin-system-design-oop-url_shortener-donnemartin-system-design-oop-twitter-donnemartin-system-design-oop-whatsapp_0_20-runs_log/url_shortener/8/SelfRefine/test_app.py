import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	# Clear mock database after each test
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

	# Test that custom short URL is already in use
	response = client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	assert response.status_code == 400

	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid'})
	assert response.status_code == 400

def test_redirect_to_url(client):
	# Test redirect to original URL
	client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	response = client.get('/custom')
	assert response.status_code == 302
	assert response.location == 'http://example.com'

	# Test URL not found
	response = client.get('/notfound')
	assert response.status_code == 404

	# Test URL has expired
	client.post('/shorten', json={'url': 'http://example.com', 'custom': 'expired', 'expiration': '2000-01-01 00:00:00'})
	response = client.get('/expired')
	assert response.status_code == 410

def test_get_analytics(client):
	# Test get analytics
	client.post('/register', json={'username': 'user', 'password': 'pass'})
	client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom', 'username': 'user'})
	client.get('/custom')
	response = client.get('/analytics?username=user')
	assert response.status_code == 200
	assert json.loads(response.data)[0]['clicks'] == 1

	# Test user not found
	response = client.get('/analytics?username=notfound')
	assert response.status_code == 404

def test_register_user(client):
	# Test register user
	response = client.post('/register', json={'username': 'user', 'password': 'pass'})
	assert response.status_code == 200

	# Test username is already taken
	response = client.post('/register', json={'username': 'user', 'password': 'pass'})
	assert response.status_code == 400

def test_admin_dashboard(client):
	# Test admin dashboard
	client.post('/register', json={'username': 'user', 'password': 'pass'})
	client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom', 'username': 'user'})
	response = client.get('/admin')
	assert response.status_code == 200
	assert len(json.loads(response.data)['urls']) == 1
	assert len(json.loads(response.data)['users']) == 1
