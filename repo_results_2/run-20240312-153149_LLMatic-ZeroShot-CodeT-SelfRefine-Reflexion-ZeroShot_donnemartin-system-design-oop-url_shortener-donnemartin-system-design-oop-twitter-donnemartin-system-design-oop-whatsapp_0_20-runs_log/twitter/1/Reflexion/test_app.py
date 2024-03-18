import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'username': 'test', 'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'User registered successfully' in response.data


def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'token' in response.data


def test_login_invalid_user(client):
	response = client.post('/login', data=json.dumps({'username': 'invalid', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert b'User does not exist' in response.data


def test_login_invalid_password(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'invalid'}), content_type='application/json')
	assert response.status_code == 400
	assert b'Invalid password' in response.data
