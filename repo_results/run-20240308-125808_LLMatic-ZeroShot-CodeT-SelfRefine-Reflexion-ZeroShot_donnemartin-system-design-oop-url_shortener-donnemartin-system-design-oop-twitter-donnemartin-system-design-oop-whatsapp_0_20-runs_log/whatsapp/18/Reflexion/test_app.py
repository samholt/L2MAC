import pytest
from app import app, users
from werkzeug.security import check_password_hash

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert 'User registered successfully' in response.get_json()['message']
	assert 'test@test.com' in users
	assert check_password_hash(users['test@test.com'], 'test123')


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert 'Logged in successfully' in response.get_json()['message']


def test_login_invalid(client):
	response = client.post('/login', json={'email': 'invalid@test.com', 'password': 'invalid'})
	assert response.status_code == 401
	assert 'Invalid email or password' in response.get_json()['message']
