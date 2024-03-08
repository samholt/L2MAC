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
	assert response.get_json() == user.to_dict()

def test_login(client, user):
	app.users[user.id] = user
	response = client.post('/login', json={'email': user.email, 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()

def test_update_profile(client, user):
	app.users[user.id] = user
	response = client.put(f'/users/{user.id}/profile', json={'profile_picture': 'picture.jpg', 'status_message': 'Hello, world!'})
	assert response.status_code == 200
	user.profile_picture = 'picture.jpg'
	user.status_message = 'Hello, world!'
	assert response.get_json() == user.to_dict()

def test_block_contact(client, user):
	contact = User('contact@example.com', 'password')
	app.users[user.id] = user
	app.users[contact.id] = contact
	response = client.post(f'/users/{user.id}/contacts', json={'contact_id': contact.id})
	assert response.status_code == 200
	user.block_contact(contact)
	assert response.get_json() == user.to_dict()

def test_create_chat(client, chat):
	response = client.post('/chats', json=chat.to_dict())
	assert response.status_code == 201
	assert response.get_json() == chat.to_dict()

def test_send_message(client, user, chat):
	app.users[user.id] = user
	app.chats[chat.id] = chat
	response = client.post(f'/chats/{chat.id}/messages', json={'user_id': user.id, 'content': 'Hello, world!'})
	assert response.status_code == 201
	message = chat.send_message(user, 'Hello, world!')
	assert response.get_json() == message.to_dict()
