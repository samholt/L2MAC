import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

	response = client.post('/register', data=json.dumps({'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Email already registered'


def test_login(client):
	response = client.post('/login', data=json.dumps({'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User logged in successfully'

	response = client.post('/login', data=json.dumps({'email': 'test@test.com', 'password': 'wrong'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid email or password'
