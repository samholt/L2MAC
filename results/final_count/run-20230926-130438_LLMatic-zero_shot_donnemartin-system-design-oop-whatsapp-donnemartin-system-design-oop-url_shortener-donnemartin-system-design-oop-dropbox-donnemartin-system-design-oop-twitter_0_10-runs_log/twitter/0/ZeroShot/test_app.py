import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def token():
	return jwt.encode({'user': 'test', 'exp': 9999999999}, app.app.config['SECRET_KEY']).decode('UTF-8')

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Username already exists'

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid username or password'

def test_post(client, token):
	response = client.post('/post', json={'user': 'test', 'text': 'Hello, world!', 'token': token})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Post created'

	response = client.post('/post', json={'user': 'test', 'text': 'This post is too long' * 100, 'token': token})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid post'
