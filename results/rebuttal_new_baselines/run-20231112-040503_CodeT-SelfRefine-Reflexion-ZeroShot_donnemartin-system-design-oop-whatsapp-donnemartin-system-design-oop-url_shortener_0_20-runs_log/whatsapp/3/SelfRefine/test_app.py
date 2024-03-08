import pytest
import app
from user import User
from chat import Chat

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user_data(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	return response.get_json()


def test_register(client):
	user_data = client.post('/register', json={'email': 'test@test.com', 'password': 'password'}).get_json()
	assert 'id' in user_data
	assert user_data['email'] == 'test@test.com'


def test_login(client, user_data):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	data = response.get_json()
	assert data['id'] == user_data['id']
	assert data['email'] == 'test@test.com'


def test_create_chat(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['name'] == 'Test Chat'
	assert data['messages'] == []


def test_send_message(client):
	chat = Chat('Test Chat')
	app.chats[chat.id] = chat
	response = client.post(f'/chat/{chat.id}/message', json={'user_id': '1', 'content': 'Hello, world!'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['user_id'] == '1'
	assert data['content'] == 'Hello, world!'
