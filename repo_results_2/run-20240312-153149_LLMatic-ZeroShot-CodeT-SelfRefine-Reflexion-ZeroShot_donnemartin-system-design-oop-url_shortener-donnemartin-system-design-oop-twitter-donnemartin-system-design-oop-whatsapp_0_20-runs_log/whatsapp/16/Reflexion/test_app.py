import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User registered successfully'

	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data)['message'] == 'Email already registered'


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User logged in successfully'

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data)['message'] == 'Invalid email or password'


def test_logout(client):
	response = client.post('/logout', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User logged out successfully'

	response = client.post('/logout', json={'email': 'test@test.com'})
	assert response.status_code == 400
	assert json.loads(response.data)['message'] == 'User not logged in'
