import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', data=json.dumps({'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}

	response = client.post('/signup', data=json.dumps({'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}
