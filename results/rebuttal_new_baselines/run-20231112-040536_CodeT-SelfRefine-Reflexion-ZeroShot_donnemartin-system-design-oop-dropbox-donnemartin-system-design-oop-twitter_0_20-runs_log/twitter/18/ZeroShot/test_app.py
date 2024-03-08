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
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

def test_update_profile(client, token):
	response = client.put('/profile', json={'token': token, 'profile': {'bio': 'test bio'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}

def test_create_post(client, token):
	response = client.post('/post', json={'token': token, 'content': 'test content'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}

def test_delete_post(client, token):
	response = client.delete('/post/0', json={'token': token})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post deleted successfully'}
