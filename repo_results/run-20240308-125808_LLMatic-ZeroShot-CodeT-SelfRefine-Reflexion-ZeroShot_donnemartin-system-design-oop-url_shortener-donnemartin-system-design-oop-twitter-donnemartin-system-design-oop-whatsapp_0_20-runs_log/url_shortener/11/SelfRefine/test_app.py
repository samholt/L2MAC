import pytest
import app
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		# Setup: Create a user and a non-expired URL for the tests
		client.post('/register', data=json.dumps({'username': 'test', 'password': 'password'}), content_type='application/json')
		expiration = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
		client.post('/shorten', data=json.dumps({'url': 'https://www.google.com', 'user': 'test', 'custom': 'google', 'expiration': expiration}), content_type='application/json')
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', data=json.dumps({'url': 'https://www.example.com', 'user': 'test', 'custom': 'example', 'expiration': '2022-12-31T23:59:59Z'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data)['shortened_url'] == 'example'


def test_redirect_url(client):
	response = client.get('/google')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.get('/analytics', data=json.dumps({'user': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert len(json.loads(response.data)['analytics']) == 2


def test_register_user(client):
	response = client.post('/register', data=json.dumps({'username': 'test2', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User registered successfully'
