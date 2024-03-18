import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'User registered successfully' in response.data


def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Logged in successfully' in response.data


def test_post(client):
	response = client.post('/post', data=json.dumps({'username': 'test', 'content': 'Hello, world!'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Post created successfully' in response.data
