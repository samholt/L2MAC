import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_logout(client):
	response = client.post('/logout', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged out successfully'}
