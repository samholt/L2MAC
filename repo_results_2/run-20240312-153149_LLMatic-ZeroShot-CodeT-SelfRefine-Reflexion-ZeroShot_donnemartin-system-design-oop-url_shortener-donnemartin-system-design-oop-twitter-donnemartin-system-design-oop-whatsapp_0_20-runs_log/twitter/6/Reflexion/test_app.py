import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_post_with_existing_user(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test123'})
	response = client.post('/post', json={'username': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Post created successfully'}


def test_post_with_non_existing_user(client):
	response = client.post('/post', json={'username': 'nonexistent', 'content': 'Hello, world!'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'User does not exist'}
