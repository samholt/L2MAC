import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert 'id' in response.get_json()

def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'id' in response.get_json()

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401

def test_user(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.get('/users/0')
	assert response.status_code == 200
	user = response.get_json()
	assert user['username'] == 'test'
	assert user['email'] == 'test@test.com'

	response = client.put('/users/0', json={'profile': {'bio': 'Hello, world!'}})
	assert response.status_code == 200
	user = response.get_json()
	assert user['profile']['bio'] == 'Hello, world!'

def test_create_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/posts', json={'user_id': 0, 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert 'id' in response.get_json()

def test_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	client.post('/posts', json={'user_id': 0, 'content': 'Hello, world!'})
	response = client.get('/posts/0')
	assert response.status_code == 200
	post = response.get_json()
	assert post['user_id'] == 0
	assert post['content'] == 'Hello, world!'

	response = client.delete('/posts/0')
	assert response.status_code == 204
	response = client.get('/posts/0')
	assert response.status_code == 404
