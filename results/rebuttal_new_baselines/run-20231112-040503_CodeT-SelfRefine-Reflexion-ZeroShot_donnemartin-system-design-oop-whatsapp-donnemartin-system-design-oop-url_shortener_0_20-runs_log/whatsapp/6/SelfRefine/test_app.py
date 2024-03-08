import pytest
import app
import json
import hashlib

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	hashed_password = hashlib.sha256('test'.encode()).hexdigest()
	response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'password': hashed_password}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'password': hashed_password}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Email already registered'}


def test_login(client):
	hashed_password = hashlib.sha256('test'.encode()).hexdigest()
	response = client.post('/login', data=json.dumps({'email': 'test@test.com', 'password': hashed_password}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User logged in successfully'}

	response = client.post('/login', data=json.dumps({'email': 'wrong@test.com', 'password': hashed_password}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json() == {'error': 'Invalid email or password'}
