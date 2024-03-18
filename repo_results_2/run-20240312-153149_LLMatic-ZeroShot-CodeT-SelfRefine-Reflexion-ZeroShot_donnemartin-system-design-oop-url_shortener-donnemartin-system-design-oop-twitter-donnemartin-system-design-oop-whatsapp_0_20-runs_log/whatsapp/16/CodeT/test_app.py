import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_login(client):
	client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert 'id' in response.get_json()


def test_create_chat(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_send_message(client):
	chat_response = client.post('/chat', json={'name': 'Test Chat'})
	chat_id = chat_response.get_json()['id']
	register_response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	user_id = register_response.get_json()['id']
	response = client.post(f'/chat/{chat_id}/message', json={'user_id': user_id, 'message': 'Hello, world!'})
	assert response.status_code == 204
