import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'status': 'success'}

	response = client.post('/register', json={'name': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'status': 'error', 'message': 'User already exists'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'status': 'success'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'status': 'error', 'message': 'Invalid credentials'}
