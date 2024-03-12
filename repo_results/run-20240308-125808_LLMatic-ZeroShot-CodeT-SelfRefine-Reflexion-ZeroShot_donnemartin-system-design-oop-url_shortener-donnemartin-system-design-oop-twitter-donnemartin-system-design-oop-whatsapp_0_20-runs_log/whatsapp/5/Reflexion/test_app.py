import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', data=json.dumps({'name': 'Test', 'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_login(client):
	response = client.post('/login', data=json.dumps({'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in'}


def test_logout(client):
	response = client.post('/logout', data=json.dumps({'email': 'test@test.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out'}
