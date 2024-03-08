import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	# Test missing email
	response = client.post('/register', json={'password': 'password'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Missing email or password'}

	# Test missing password
	response = client.post('/register', json={'email': 'test@test.com'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Missing email or password'}

	# Test successful registration
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}

	# Test duplicate registration
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Email already registered'}
