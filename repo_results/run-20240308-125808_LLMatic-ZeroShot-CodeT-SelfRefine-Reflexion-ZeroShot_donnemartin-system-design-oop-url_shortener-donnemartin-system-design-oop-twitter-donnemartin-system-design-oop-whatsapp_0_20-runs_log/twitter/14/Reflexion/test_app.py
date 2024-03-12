import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True

	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert b'User created' in response.data


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert b'access_token' in response.data


def test_post(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = json.loads(response.data)['access_token']

	response = client.post('/post', json={'content': 'Hello, world!'}, headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 201
	assert b'Post created' in response.data
