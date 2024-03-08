import pytest
import app
from flask import Flask

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()


def test_login_fail(client):
	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}
