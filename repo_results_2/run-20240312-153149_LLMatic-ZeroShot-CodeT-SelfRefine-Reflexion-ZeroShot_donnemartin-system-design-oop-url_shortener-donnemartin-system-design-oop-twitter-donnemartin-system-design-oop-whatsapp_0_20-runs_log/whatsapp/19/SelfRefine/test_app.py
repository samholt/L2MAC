import pytest
import app
from user import User
from chat import Chat

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['email'] == 'test@example.com'


def test_login(client):
	response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	data = response.get_json()
	user_id = data['id']
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	data = response.get_json()
	assert data['id'] == user_id
	assert data['email'] == 'test@example.com'


def test_create_chat(client):
	response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	data = response.get_json()
	user_id = data['id']
	response = client.post(f'/users/{user_id}/chats', json={'name': 'Test Chat'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['name'] == 'Test Chat'
	assert data['users'] == [user_id]
	assert data['messages'] == []


def test_send_message(client):
	response = client.post('/register', json={'email': 'test@example.com', 'password': 'password'})
	data = response.get_json()
	user_id = data['id']
	response = client.post(f'/users/{user_id}/chats', json={'name': 'Test Chat'})
	data = response.get_json()
	chat_id = data['id']
	response = client.post(f'/users/{user_id}/chats/{chat_id}/messages', json={'content': 'Hello, world!'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['user_id'] == user_id
	assert data['content'] == 'Hello, world!'
