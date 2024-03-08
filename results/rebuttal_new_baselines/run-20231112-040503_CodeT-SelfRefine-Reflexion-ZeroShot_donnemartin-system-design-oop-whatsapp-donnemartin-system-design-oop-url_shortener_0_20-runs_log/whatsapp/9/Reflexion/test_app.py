import pytest
import app
from flask import json

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

	response = client.post('/register', data=json.dumps({'email': '', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Missing email or password'
