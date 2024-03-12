import pytest
import app
from flask import json
from datetime import datetime, timedelta

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

def test_shorten_url(client):
	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'short_url': 'goog', 'username': 'test', 'password': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'URL shortened successfully'}

	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'short_url': 'goog', 'username': 'test', 'password': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Short URL already exists'}

	response = client.post('/shorten_url', json={'original_url': 'https://www.invalidurl.com', 'short_url': 'invalid', 'username': 'test', 'password': 'test', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid original URL'}

	response = client.post('/shorten_url', json={'original_url': 'https://www.google.com', 'short_url': 'goog', 'username': 'test', 'password': 'wrong', 'expiration': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid username or password'}

def test_redirect_url(client):
	response = client.get('/goog')
	assert response.status_code == 302

	response = client.get('/invalid')
	assert response.status_code == 404
	assert json.loads(response.data) == {'message': 'Invalid or expired short URL'}

	response = client.get('/nonexistent')
	assert response.status_code == 404
	assert json.loads(response.data) == {'message': 'Invalid or expired short URL'}

def test_get_analytics(client):
	response = client.get('/analytics?username=test&password=test')
	assert response.status_code == 200
	analytics = json.loads(response.data)
	assert 'goog' in analytics
	assert analytics['goog']['clicks'] == 1

	response = client.get('/analytics?username=nonexistent&password=test')
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid username or password'}

	response = client.get('/analytics?username=test&password=wrong')
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid username or password'}
