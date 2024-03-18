import pytest
from app import app, users, posts

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}
	assert len(users) == 1


def test_register_existing_email(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/register', json={'username': 'test2', 'email': 'test@test.com', 'password': 'test2'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already registered'}


def test_login(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_login_invalid_credentials(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid credentials'}


def test_post(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/post', json={'user_id': 1, 'content': 'Hello, world!'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}
	assert len(posts) == 1


def test_post_exceed_character_limit(client):
	client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	response = client.post('/post', json={'user_id': 1, 'content': 'a' * 281})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Post content exceeds character limit'}
