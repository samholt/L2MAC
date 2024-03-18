import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'id' in data
	assert data['email'] == 'test@test.com'


def test_login(client):
	client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	data = json.loads(response.data)
	assert 'id' in data
	assert data['email'] == 'test@test.com'


def test_create_chat(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	user_id = json.loads(response.data)['id']
	response = client.post(f'/users/{user_id}/chats', json={'name': 'Test Chat'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'id' in data
	assert data['name'] == 'Test Chat'
	assert len(data['users']) == 1
	assert data['users'][0]['id'] == user_id


def test_send_message(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	user_id = json.loads(response.data)['id']
	response = client.post(f'/users/{user_id}/chats', json={'name': 'Test Chat'})
	chat_id = json.loads(response.data)['id']
	response = client.post(f'/users/{user_id}/chats/{chat_id}/messages', json={'content': 'Hello, world!'})
	assert response.status_code == 201
	data = json.loads(response.data)
	assert 'id' in data
	assert data['user']['id'] == user_id
	assert data['content'] == 'Hello, world!'
