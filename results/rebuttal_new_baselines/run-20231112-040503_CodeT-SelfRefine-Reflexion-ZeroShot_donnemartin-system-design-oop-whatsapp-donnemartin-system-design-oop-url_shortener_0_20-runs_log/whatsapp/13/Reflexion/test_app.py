import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_send_message(client):
	response = client.post('/send_message', json={'sender': 'test@test.com', 'message': 'Hello, World!'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Message sent successfully'}


def test_get_messages(client):
	response = client.get('/get_messages')
	assert response.status_code == 200
	assert 'test@test.com' in json.loads(response.data)
