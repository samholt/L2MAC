import pytest
import app
import hashlib

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}
	response = client.post('/signup', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already in use'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}
	client.post('/signup', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_logout(client):
	response = client.post('/logout', json={'email': 'test@example.com'})
	assert response.status_code == 404
	assert response.get_json() == {'message': 'User not found'}
	client.post('/signup', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	response = client.post('/logout', json={'email': 'test@example.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out successfully'}
