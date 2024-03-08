import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Registered successfully'


def test_login(client):
	client.post('/register', json={'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'})
	response = client.post('/login', json={'email': 'testuser@example.com', 'password': 'testpassword'})
	assert response.status_code == 200
	assert 'token' in json.loads(response.data)


def test_login_invalid_credentials(client):
	client.post('/register', json={'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'})
	response = client.post('/login', json={'email': 'testuser@example.com', 'password': 'wrongpassword'})
	assert response.status_code == 401
	assert json.loads(response.data)['message'] == 'Invalid credentials'
