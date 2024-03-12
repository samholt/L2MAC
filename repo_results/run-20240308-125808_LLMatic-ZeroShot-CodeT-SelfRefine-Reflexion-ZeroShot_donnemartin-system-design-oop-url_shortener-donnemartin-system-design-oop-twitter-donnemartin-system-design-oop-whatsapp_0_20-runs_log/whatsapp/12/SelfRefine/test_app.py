import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

	# Try to register with the same email
	response = client.post('/register', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already in use'}


def test_login(client):
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_login_invalid(client):
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'wrongpassword'}), content_type='application/json')
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid email or password'}
