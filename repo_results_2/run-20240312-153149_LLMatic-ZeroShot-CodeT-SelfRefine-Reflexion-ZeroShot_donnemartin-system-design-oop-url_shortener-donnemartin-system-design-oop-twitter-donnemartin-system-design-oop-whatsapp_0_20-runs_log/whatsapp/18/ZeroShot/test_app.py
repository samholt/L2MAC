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
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert 'id' in response.get_json()

def test_login(client):
	user = User('test@test.com', 'test')
	app.users[user.id] = user
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json()['id'] == user.id

def test_forgot_password(client):
	user = User('test@test.com', 'test')
	app.users[user.id] = user
	response = client.post('/forgot_password', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password reset'

def test_user_profile(client):
	user = User('test@test.com', 'test')
	app.users[user.id] = user
	response = client.get(f'/users/{user.id}/profile')
	assert response.status_code == 200
	assert response.get_json()['id'] == user.id

def test_block_user(client):
	user = User('test@test.com', 'test')
	blocked_user = User('blocked@test.com', 'test')
	app.users[user.id] = user
	app.users[blocked_user.id] = blocked_user
	response = client.post(f'/users/{user.id}/block', json={'blocked_user_id': blocked_user.id})
	assert response.status_code == 200
	assert blocked_user.id in response.get_json()['blocked_users']

def test_create_chat(client):
	user = User('test@test.com', 'test')
	app.users[user.id] = user
	response = client.post(f'/users/{user.id}/chats')
	assert response.status_code == 201
	assert 'id' in response.get_json()

def test_manage_chat(client):
	user = User('test@test.com', 'test')
	chat = Chat([user.id])
	app.users[user.id] = user
	app.chats[chat.id] = chat
	response = client.get(f'/chats/{chat.id}')
	assert response.status_code == 200
	assert response.get_json()['id'] == chat.id
