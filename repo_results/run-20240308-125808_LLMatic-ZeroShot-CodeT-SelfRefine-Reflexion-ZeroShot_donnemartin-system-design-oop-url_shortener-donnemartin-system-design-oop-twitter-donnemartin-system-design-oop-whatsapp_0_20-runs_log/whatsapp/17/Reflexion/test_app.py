import pytest
import app
from models.user import User
from models.chat import Chat

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'id': '1', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_update_user_settings(client):
	response = client.put('/user/1/settings', json={'profile_picture': 'picture.jpg', 'status_message': 'Hello', 'privacy_settings': {'last_seen': 'everyone'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User settings updated successfully'}


def test_block_contact(client):
	response = client.post('/user/1/block', json={'contact': '2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact blocked successfully'}


def test_unblock_contact(client):
	response = client.post('/user/1/unblock', json={'contact': '2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact unblocked successfully'}


def test_create_chat(client):
	response = client.post('/chat', json={'id': '1', 'members': ['1', '2']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Chat created successfully'}


def test_add_chat_member(client):
	response = client.post('/chat/1/member', json={'member': '3'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Member added successfully'}


def test_remove_chat_member(client):
	response = client.delete('/chat/1/member', json={'member': '2'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Member removed successfully'}


def test_send_message(client):
	response = client.post('/chat/1/message', json={'message': 'Hello'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent successfully'}
