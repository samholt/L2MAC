import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}

	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Email already in use'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid email or password'}
