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
	assert 'id' in response.get_json()


def test_login(client):
	user = User('test@example.com', 'password')
	app.users[user.email] = user
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json()['id'] == user.id


def test_create_chat(client):
	user = User('test@example.com', 'password')
	app.users[user.email] = user
	response = client.post(f'/users/{user.id}/chats', json={'name': 'Test Chat'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_send_message(client):
	user = User('test@example.com', 'password')
	app.users[user.email] = user
	chat = Chat('Test Chat')
	chat.add_user(user.id)
	app.chats[chat.id] = chat
	response = client.post(f'/users/{user.id}/chats/{chat.id}/messages', json={'content': 'Hello, world!'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
