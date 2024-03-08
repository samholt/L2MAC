import pytest
import app
from app import User, Chat

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'John', 'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert app.users['john@example.com'].name == 'John'


def test_login(client):
	app.users['john@example.com'] = User(name='John', email='john@example.com', password='password')
	response = client.post('/login', json={'email': 'john@example.com', 'password': 'password'})
	assert response.status_code == 200


def test_create_chat(client):
	response = client.post('/chats', json={'id': 1, 'users': ['john@example.com']})
	assert response.status_code == 201
	assert app.chats[1].id == 1


def test_send_message(client):
	app.chats[1] = Chat(id=1, users=['john@example.com'], messages=[])
	response = client.post('/chats/1/messages', json={'user': 'john@example.com', 'message': 'Hello'})
	assert response.status_code == 201
	assert app.chats[1].messages[0] == 'Hello'
