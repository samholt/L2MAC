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
	response = client.post('/login', json={'email': user.email, 'password': user.password})
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()

def test_forgot_password(client, user):
	app.users[user.id] = user
	response = client.post('/forgot_password', json={'email': user.email})
	assert response.status_code == 200
	assert user.password == 'new_password'

def test_profile(client, user):
	app.users[user.id] = user
	response = client.get(f'/users/{user.id}/profile')
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()

def test_block_unblock_contact(client, user):
	contact = User('contact@example.com', 'password')
	app.users[user.id] = user
	app.users[contact.id] = contact
	response = client.post(f'/users/{user.id}/contacts', json={'contact_id': contact.id, 'action': 'block'})
	assert response.status_code == 200
	assert contact.id in user.blocked_contacts
	response = client.post(f'/users/{user.id}/contacts', json={'contact_id': contact.id, 'action': 'unblock'})
	assert response.status_code == 200
	assert contact.id not in user.blocked_contacts

def test_create_chat(client, chat):
	response = client.post('/chats', json=chat.to_dict())
	assert response.status_code == 201
	assert response.get_json() == chat.to_dict()

def test_manage_chat(client, chat):
	app.chats[chat.id] = chat
	response = client.get(f'/chats/{chat.id}')
	assert response.status_code == 200
	assert response.get_json() == chat.to_dict()
