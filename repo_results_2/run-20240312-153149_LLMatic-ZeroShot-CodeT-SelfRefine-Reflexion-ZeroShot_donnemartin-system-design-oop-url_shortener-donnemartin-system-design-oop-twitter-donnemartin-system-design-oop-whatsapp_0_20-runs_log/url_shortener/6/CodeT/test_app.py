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
	response = client.post('/shorten', json={'url': 'http://example.com'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'shortened_url' in data

	# Test with custom alias
	response = client.post('/shorten', json={'url': 'http://example.com', 'alias': 'custom'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert data['shortened_url'] == 'custom'

	# Test with duplicate alias
	response = client.post('/shorten', json={'url': 'http://example.com', 'alias': 'custom'})
	assert response.status_code == 400


def test_redirect_url(client):
	# Shorten URL first
	response = client.post('/shorten', json={'url': 'http://example.com'})
	data = json.loads(response.data)
	shortened_url = data['shortened_url']

	# Test redirection
	response = client.get(f'/{shortened_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	# Register user first
	response = client.post('/register', json={'username': 'test', 'password': 'test'})

	# Shorten URL
	response = client.post('/shorten', json={'url': 'http://example.com', 'username': 'test'})

	# Get analytics
	response = client.get('/analytics?username=test')
	assert response.status_code == 200
	data = json.loads(response.data)
	assert len(data) == 1
	assert data[0]['clicks'] == 0


def test_register_user(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200

	# Test with duplicate username
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
