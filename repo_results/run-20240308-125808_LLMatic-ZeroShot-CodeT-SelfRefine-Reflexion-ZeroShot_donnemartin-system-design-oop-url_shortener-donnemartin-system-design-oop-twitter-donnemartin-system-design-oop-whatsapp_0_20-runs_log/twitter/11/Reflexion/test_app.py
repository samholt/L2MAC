import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'username': 'test', 'email': 'test@test.com', 'password': 'test', 'profile': {}})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Login successful'}


def test_post(client):
	response = client.post('/post', json={'id': '1', 'user_id': '1', 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Post created successfully'}


def test_like(client):
	response = client.post('/like', json={'post_id': '1'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Post liked'}
