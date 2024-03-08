import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'User created'}


def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in json.loads(response.data)


def test_protected(client):
	response = client.get('/protected')
	assert response.status_code == 401
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = json.loads(response.data)['access_token']
	headers = {'Authorization': f'Bearer {access_token}'}
	response = client.get('/protected', headers=headers)
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Access granted'}
