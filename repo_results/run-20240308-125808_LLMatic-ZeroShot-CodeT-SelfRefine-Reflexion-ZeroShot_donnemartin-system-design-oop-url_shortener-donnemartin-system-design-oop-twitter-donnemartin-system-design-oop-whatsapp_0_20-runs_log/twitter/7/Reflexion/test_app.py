import pytest
import app
import json
from flask import Flask

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
	assert b'token' in response.data


def test_update_profile(client):
	response = client.put('/profile', data=json.dumps({'username': 'test', 'bio': 'This is a test bio'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Profile updated successfully' in response.data


def test_create_post(client):
	response = client.post('/post', data=json.dumps({'username': 'test', 'content': 'This is a test post'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Post created successfully' in response.data


def test_delete_post(client):
	response = client.delete('/post/1')
	assert response.status_code == 200
	assert b'Post deleted successfully' in response.data
