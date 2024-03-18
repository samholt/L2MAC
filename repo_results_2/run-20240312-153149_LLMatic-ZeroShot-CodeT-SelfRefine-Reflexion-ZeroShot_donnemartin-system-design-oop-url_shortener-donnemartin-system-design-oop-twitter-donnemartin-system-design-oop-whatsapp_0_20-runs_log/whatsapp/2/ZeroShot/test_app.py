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
def chat(user):
	return Chat('Test Chat', [user.id])

def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 201
	assert 'id' in response.get_json()

def test_login(client, user):
	app.users[user.id] = user
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert 'id' in response.get_json()

def test_forgot_password(client, user):
	app.users[user.id] = user
	response = client.post('/forgot_password', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password reset successful'

def test_get_user(client, user):
	app.users[user.id] = user
	response = client.get(f'/users/{user.id}')
	assert response.status_code == 200
	assert 'id' in response.get_json()

def test_update_user(client, user):
	app.users[user.id] = user
	response = client.put(f'/users/{user.id}', json={'profile_picture': 'new_picture.jpg', 'status_message': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json()['profile_picture'] == 'new_picture.jpg'
	assert response.get_json()['status_message'] == 'Hello, world!'

def test_block_user(client, user):
	blocked_user = User('blocked@test.com', 'password')
	app.users[user.id] = user
	app.users[blocked_user.id] = blocked_user
	response = client.post(f'/users/{user.id}/block', json={'blocked_user_id': blocked_user.id})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User blocked successfully'

def test_unblock_user(client, user):
	unblocked_user = User('unblocked@test.com', 'password')
	user.block_user(unblocked_user)
	app.users[user.id] = user
	app.users[unblocked_user.id] = unblocked_user
	response = client.post(f'/users/{user.id}/unblock', json={'unblocked_user_id': unblocked_user.id})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User unblocked successfully'

def test_create_chat(client, user):
	app.users[user.id] = user
	response = client.post('/chats', json={'name': 'Test Chat', 'user_ids': [user.id]})
	assert response.status_code == 201
	assert 'id' in response.get_json()

def test_get_chat(client, chat):
	app.chats[chat.id] = chat
	response = client.get(f'/chats/{chat.id}')
	assert response.status_code == 200
	assert 'id' in response.get_json()

def test_update_chat(client, chat):
	app.chats[chat.id] = chat
	response = client.put(f'/chats/{chat.id}', json={'name': 'Updated Chat'})
	assert response.status_code == 200
	assert response.get_json()['name'] == 'Updated Chat'

def test_send_message(client, chat, user):
	app.chats[chat.id] = chat
	app.users[user.id] = user
	response = client.post(f'/chats/{chat.id}/messages', json={'user_id': user.id, 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert 'id' in response.get_json()
