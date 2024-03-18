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
	return User('test@test.com', 'password')

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

def test_user(client, user):
	app.users[user.id] = user
	response = client.get(f'/users/{user.id}')
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()
	response = client.put(f'/users/{user.id}', json={'profile_picture': 'new_picture.jpg', 'status_message': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == user.to_dict()

def test_block_user(client, user):
	app.users[user.id] = user
	user_to_block = User('block@test.com', 'password')
	app.users[user_to_block.id] = user_to_block
	response = client.post(f'/users/{user.id}/block', json={'user_to_block': user_to_block.id})
	assert response.status_code == 200
	assert user_to_block.id in user.blocked_users

def test_unblock_user(client, user):
	app.users[user.id] = user
	user_to_unblock = User('unblock@test.com', 'password')
	app.users[user_to_unblock.id] = user_to_unblock
	user.block_user(user_to_unblock)
	response = client.post(f'/users/{user.id}/unblock', json={'user_to_unblock': user_to_unblock.id})
	assert response.status_code == 200
	assert user_to_unblock.id not in user.blocked_users

def test_create_chat(client, chat):
	response = client.post('/chats', json=chat.to_dict())
	assert response.status_code == 201
	assert response.get_json() == chat.to_dict()

def test_chat(client, chat):
	app.chats[chat.id] = chat
	response = client.get(f'/chats/{chat.id}')
	assert response.status_code == 200
	assert response.get_json() == chat.to_dict()
	response = client.put(f'/chats/{chat.id}', json={'name': 'New Chat Name'})
	assert response.status_code == 200
	assert response.get_json() == chat.to_dict()

def test_add_user_to_chat(client, user, chat):
	app.users[user.id] = user
	app.chats[chat.id] = chat
	response = client.post(f'/chats/{chat.id}/add_user', json={'user_to_add': user.id})
	assert response.status_code == 200
	assert user.id in chat.users

def test_remove_user_from_chat(client, user, chat):
	app.users[user.id] = user
	app.chats[chat.id] = chat
	chat.add_user(user)
	response = client.post(f'/chats/{chat.id}/remove_user', json={'user_to_remove': user.id})
	assert response.status_code == 200
	assert user.id not in chat.users
