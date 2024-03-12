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
	return jwt.encode({'user_id': 0}, 'secret', algorithm='HS256')


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Username or email already in use'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()


def test_post(client, token):
	response = client.post('/post', json={'user_id': 0, 'content': 'Hello, world!', 'token': token})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Post created successfully'}
