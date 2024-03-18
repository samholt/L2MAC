import pytest
import app
import hashlib

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_register_duplicate_email(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already in use'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()


def test_login_fail(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'wrongpassword'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid email or password'}


def test_protected_route(client):
	response = client.get('/protected')
	assert response.status_code == 401
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	access_token = response.get_json()['access_token']
	response = client.get('/protected', headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Access granted'}
