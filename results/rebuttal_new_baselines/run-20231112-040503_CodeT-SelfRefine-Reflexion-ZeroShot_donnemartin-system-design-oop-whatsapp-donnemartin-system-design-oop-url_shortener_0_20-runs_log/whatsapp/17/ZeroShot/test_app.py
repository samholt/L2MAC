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
	data = json.loads(response.data)
	assert 'id' in data
	assert data['email'] == 'test@example.com'


def test_login(client):
	client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'id' in data
	assert data['email'] == 'test@example.com'


def test_create_chat(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'id' in data
	assert data['name'] == 'Test Chat'
	assert data['messages'] == []


def test_send_message(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	chat_id = json.loads(response.data)['id']
	response = client.post(f'/chat/{chat_id}/message', json={'user_id': '1', 'content': 'Hello, world!'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'id' in data
	assert data['user_id'] == '1'
	assert data['content'] == 'Hello, world!'
