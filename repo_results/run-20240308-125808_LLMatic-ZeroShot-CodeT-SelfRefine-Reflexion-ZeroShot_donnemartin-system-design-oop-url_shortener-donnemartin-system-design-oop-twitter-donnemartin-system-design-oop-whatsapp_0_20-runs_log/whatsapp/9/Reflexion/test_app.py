import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}

	# Test registering the same user again
	response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'User already exists'}

def test_login(client):
	# Test logging in before registering
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid email or password'}

	# Register a user
	client.post('/register', json={'email': 'test@example.com', 'password': 'password'})

	# Test logging in with wrong password
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'wrong_password'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid email or password'}

	# Test logging in with correct password
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}

def test_forgot_password(client):
	# Test forgetting password before registering
	response = client.post('/forgot_password', json={'email': 'test@example.com'})
	assert response.status_code == 404
	assert json.loads(response.data) == {'message': 'User not found'}

	# Register a user
	client.post('/register', json={'email': 'test@example.com', 'password': 'password'})

	# Test forgetting password after registering
	response = client.post('/forgot_password', json={'email': 'test@example.com'})
	assert response.status_code == 200
	assert 'reset_link' in json.loads(response.data)
