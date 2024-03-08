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
	assert response.get_json()['message'] == 'User registered successfully'

	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'

	response = client.get('/users/1')
	assert response.status_code == 200
	user = response.get_json()
	assert user['id'] == 1
	assert user['username'] == 'test'
	assert user['email'] == 'test@test.com'

	response = client.put('/users/1', json={'bio': 'Test bio', 'website': 'https://test.com', 'location': 'Test location', 'is_private': True})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User updated successfully'

	response = client.get('/users/1')
	assert response.status_code == 200
	user = response.get_json()
	assert user['bio'] == 'Test bio'
	assert user['website'] == 'https://test.com'
	assert user['location'] == 'Test location'
	assert user['is_private'] == True

	response = client.post('/posts', json={'user_id': 1, 'content': 'Test post'})
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Post created successfully'

	response = client.get('/posts/1')
	assert response.status_code == 200
	post = response.get_json()
	assert post['id'] == 1
	assert post['user_id'] == 1
	assert post['content'] == 'Test post'

	response = client.delete('/posts/1')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Post deleted successfully'

	response = client.get('/posts/1')
	assert response.status_code == 404
	assert response.get_json()['message'] == 'Post not found'
