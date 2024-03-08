import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'


def test_register_without_email(client):
	response = client.post('/register', data=json.dumps({'name': 'Test User', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Email is required'
