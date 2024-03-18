import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Registered successfully' in response.data


def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'token' in response.data


def test_login_fail(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'wrong'}), content_type='application/json')
	assert response.status_code == 401
	assert b'Invalid username or password' in response.data
