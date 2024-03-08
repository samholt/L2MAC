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
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/post', json={'username': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}


def test_get_posts(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	client.post('/post', json={'username': 'test', 'content': 'Hello, world!'})
	response = client.get('/posts')
	assert response.status_code == 200
	assert response.get_json() == {'posts': ['Hello, world!']}
