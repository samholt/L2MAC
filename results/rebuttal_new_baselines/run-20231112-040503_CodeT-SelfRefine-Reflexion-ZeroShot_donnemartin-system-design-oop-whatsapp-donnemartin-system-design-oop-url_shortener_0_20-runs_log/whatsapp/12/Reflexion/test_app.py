import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user', json={'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'status': 'User created'}


def test_create_chat(client):
	response = client.post('/create_chat', json={'id': 1, 'members': ['john@example.com'], 'messages': []})
	assert response.status_code == 201
	assert json.loads(response.data) == {'status': 'Chat created'}


def test_send_message(client):
	client.post('/create_chat', json={'id': 1, 'members': ['john@example.com'], 'messages': []})
	response = client.post('/send_message', json={'chat_id': 1, 'message': 'Hello, world!'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'status': 'Message sent'}
