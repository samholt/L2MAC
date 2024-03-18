import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'email': 'test2@test.com', 'password': 'test2'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username already exists'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = client.post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_post(client):
	token = jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')
	response = client.post('/post', json={'token': token, 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}

	response = client.post('/post', json={'token': 'wrong', 'content': 'Hello, world!'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid token'}
