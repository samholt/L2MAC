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
def user():
	return User('test@example.com', 'password')

@pytest.fixture
def chat():
	return Chat('Test Chat')

def test_register(client, user):
	response = client.post('/register', json=user.to_dict())
	assert response.status_code == 201
	assert response.get_json()['email'] == user.email

def test_login(client, user):
	app.users[user.id] = user
	response = client.post('/login', json={'email': user.email, 'password': user.password})
	assert response.status_code == 200
	assert response.get_json()['email'] == user.email

def test_create_chat(client, user, chat):
	app.users[user.id] = user
	response = client.post(f'/users/{user.id}/chats', json=chat.to_dict())
	assert response.status_code == 201
	assert response.get_json()['name'] == chat.name

def test_send_message(client, user, chat):
	app.users[user.id] = user
	app.chats[chat.id] = chat
	response = client.post(f'/users/{user.id}/chats/{chat.id}/messages', json={'content': 'Hello, World!'})
	assert response.status_code == 201
	assert response.get_json()['content'] == 'Hello, World!'
