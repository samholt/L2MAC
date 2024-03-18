import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}

	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Email already registered'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'wrong@test.com', 'password': 'test123'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Invalid email or password'}
