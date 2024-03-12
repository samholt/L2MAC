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
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_login(client):
	user = User('test@test.com', 'password')
	app.users[user.id] = user
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json()['id'] == user.id


def test_update_profile(client):
	user = User('test@test.com', 'password')
	app.users[user.id] = user
	response = client.put(f'/users/{user.id}/profile', json={'profile_picture': 'picture.jpg', 'status_message': 'Hello'})
	assert response.status_code == 200
	assert response.get_json()['profile_picture'] == 'picture.jpg'
	assert response.get_json()['status_message'] == 'Hello'


def test_block_contact(client):
	user = User('test@test.com', 'password')
	app.users[user.id] = user
	response = client.post(f'/users/{user.id}/contacts', json={'contact_id': 'contact_id'})
	assert response.status_code == 200
	assert 'contact_id' in response.get_json()['blocked_contacts']


def test_create_chat(client):
	response = client.post('/chats', json={'name': 'Test Chat', 'user_ids': ['user_id']})
	assert response.status_code == 201
	assert 'id' in response.get_json()


def test_send_message(client):
	chat = Chat('Test Chat', ['user_id'])
	app.chats[chat.id] = chat
	response = client.post(f'/chats/{chat.id}/messages', json={'user_id': 'user_id', 'content': 'Hello'})
	assert response.status_code == 200
	assert response.get_json()['messages'][0]['content'] == 'Hello'
