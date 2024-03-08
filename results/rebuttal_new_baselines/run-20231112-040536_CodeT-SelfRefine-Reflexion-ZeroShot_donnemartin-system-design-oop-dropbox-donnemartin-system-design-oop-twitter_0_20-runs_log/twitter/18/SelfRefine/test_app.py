import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'User already exists'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in json.loads(response.data)

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password'}

	response = client.post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid username or password'}

def test_post(client):
	response = client.post('/post', json={'user': 'test', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Post created successfully'}

	response = client.post('/post', json={'user': 'test', 'content': 'Hello, world!' * 100})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Post content exceeds 280 characters'}

	response = client.post('/post', json={'user': 'wrong', 'content': 'Hello, world!'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid user'}

def test_get_posts(client):
	response = client.get('/posts')
	assert response.status_code == 200
	assert isinstance(json.loads(response.data), dict)
