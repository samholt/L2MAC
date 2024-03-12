import pytest
import app
from user import User
from chat import Chat, Message

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return User('test@test.com', 'password')

@pytest.fixture
def chat():
	return Chat('Test Chat')

@pytest.fixture
def message(user):
	return Message(user.id, 'Hello, World!')


def test_register(client, user):
	response = client.post('/register', json={'email': user.email, 'password': user.password})
	assert response.status_code == 201
	assert response.get_json() == {'id': response.get_json()['id'], 'email': user.email}


def test_login(client, user):
	app.users[user.id] = user
	response = client.post('/login', json={'email': user.email, 'password': user.password})
	assert response.status_code == 200
	assert response.get_json() == {'id': user.id, 'email': user.email}


def test_create_chat(client, chat):
	response = client.post('/chat', json={'name': chat.name})
	assert response.status_code == 201
	assert response.get_json() == {'id': response.get_json()['id'], 'name': chat.name, 'messages': []}


def test_send_message(client, chat, user, message):
	app.chats[chat.id] = chat
	response = client.post(f'/chat/{chat.id}/message', json={'user_id': user.id, 'content': message.content})
	assert response.status_code == 201
	assert response.get_json() == {'id': response.get_json()['id'], 'user_id': user.id, 'content': message.content}
