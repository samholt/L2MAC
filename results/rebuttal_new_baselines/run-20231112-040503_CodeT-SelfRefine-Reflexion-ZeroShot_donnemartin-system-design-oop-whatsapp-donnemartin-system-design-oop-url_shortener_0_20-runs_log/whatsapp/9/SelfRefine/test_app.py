import pytest
import app

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
	client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already in use'}


def test_login(client):
	client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Login successful'}


def test_login_invalid(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'wrongpassword'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid email or password'}
