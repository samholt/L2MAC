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
	short_url = json.loads(response.data)['short_url']
	assert short_url in app.urls

	# Test custom short URL
	response = client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	assert response.status_code == 200
	assert 'custom' in app.urls

	# Test custom short URL that's already taken
	response = client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	assert response.status_code == 400

	# Test URL that's already been shortened
	response = client.post('/shorten', json={'url': 'http://example.com'})
	assert response.status_code == 200
	assert json.loads(response.data)['short_url'] == short_url


def test_redirect_url(client):
	# Test redirecting to original URL
	client.post('/shorten', json={'url': 'http://example.com'})
	response = client.get('/' + list(app.urls.keys())[0])
	assert response.status_code == 302

	# Test non-existent short URL
	response = client.get('/nonexistent')
	assert response.status_code == 404


def test_get_analytics(client):
	# Test getting analytics for non-existent user
	response = client.get('/analytics?username=nonexistent')
	assert response.status_code == 404

	# Test getting analytics for existing user
	client.post('/register', json={'username': 'test', 'password': 'test'})
	client.post('/shorten', json={'url': 'http://example.com', 'username': 'test'})
	response = client.get('/analytics?username=test')
	assert response.status_code == 200
	assert len(json.loads(response.data)) == 1


def test_register_user(client):
	# Test registering user
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'test' in app.users

	# Test registering user with username that's already taken
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
