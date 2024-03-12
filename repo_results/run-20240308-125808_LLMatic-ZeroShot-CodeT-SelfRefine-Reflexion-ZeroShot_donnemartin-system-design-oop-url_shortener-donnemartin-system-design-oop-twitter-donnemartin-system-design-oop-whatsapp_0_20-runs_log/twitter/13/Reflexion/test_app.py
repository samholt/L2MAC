import pytest
from app import app, User, Post, users, posts

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert 'User registered successfully' in response.get_json()['message']
	assert 'test' in users


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'Logged in successfully' in response.get_json()['message']


def test_post(client):
	response = client.post('/post', json={'user_id': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert 'Post created successfully' in response.get_json()['message']
	assert 'test' in posts
