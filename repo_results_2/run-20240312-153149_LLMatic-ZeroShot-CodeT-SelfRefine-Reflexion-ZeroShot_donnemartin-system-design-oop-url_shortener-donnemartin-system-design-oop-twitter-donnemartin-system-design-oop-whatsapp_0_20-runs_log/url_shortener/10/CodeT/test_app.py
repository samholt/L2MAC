import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client

	# Cleanup after test
	app.users = {}
	app.urls = {}


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

	# Test invalid URL
	response = client.post('/shorten', json={'url': 'invalid'})
	assert response.status_code == 400

	# Test taken custom short URL
	response = client.post('/shorten', json={'url': 'http://example.com', 'custom': 'custom'})
	assert response.status_code == 400


def test_redirect_to_original(client):
	# Test redirection
	client.post('/shorten', json={'url': 'http://example.com'})
	response = client.get('/' + list(app.urls.keys())[0])
	assert response.status_code == 302

	# Test non-existent URL
	response = client.get('/nonexistent')
	assert response.status_code == 404


def test_create_user(client):
	# Test user creation
	response = client.post('/user', json={'username': 'user', 'password': 'pass'})
	assert response.status_code == 200
	assert 'user' in app.users

	# Test taken username
	response = client.post('/user', json={'username': 'user', 'password': 'pass'})
	assert response.status_code == 400


def test_get_user(client):
	# Test get user
	client.post('/user', json={'username': 'user', 'password': 'pass'})
	response = client.get('/user/user')
	assert response.status_code == 200

	# Test non-existent user
	response = client.get('/user/nonexistent')
	assert response.status_code == 404
