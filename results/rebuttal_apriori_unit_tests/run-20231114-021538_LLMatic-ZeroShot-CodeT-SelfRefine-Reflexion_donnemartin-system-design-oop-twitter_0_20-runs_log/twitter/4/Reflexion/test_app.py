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
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_profile(client):
	response = client.get('/profile/1')
	assert response.status_code == 200
	assert json.loads(response.data) == {}

	response = client.put('/profile/1', json={'bio': 'Test bio', 'website': 'https://test.com', 'location': 'Test location'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'bio': 'Test bio', 'website': 'https://test.com', 'location': 'Test location'}


def test_post(client):
	response = client.post('/post', json={'user_id': 1, 'content': 'Test post'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Post created successfully'}


def test_get_post(client):
	response = client.get('/post/1')
	assert response.status_code == 200
	assert json.loads(response.data) == {'id': 1, 'user_id': 1, 'content': 'Test post', 'likes': 0, 'retweets': 0, 'replies': []}

	response = client.delete('/post/1')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Post deleted successfully'}
