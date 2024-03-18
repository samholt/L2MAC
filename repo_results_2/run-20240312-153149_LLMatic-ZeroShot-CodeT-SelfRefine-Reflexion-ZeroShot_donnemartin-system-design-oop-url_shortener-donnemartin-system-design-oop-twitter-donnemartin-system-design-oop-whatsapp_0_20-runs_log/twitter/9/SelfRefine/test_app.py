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
	return jwt.encode({'user': 'test', 'exp': 9999999999}, app.app.config['SECRET_KEY'])

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

def test_post(client, token):
	response = client.post('/post', json={'user': 'test', 'text': 'Hello, world!', 'token': token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created'}

def test_get_posts(client):
	response = client.get('/posts')
	assert response.status_code == 200
	assert isinstance(response.get_json(), dict)
