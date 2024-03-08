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
	assert response.get_json()['email'] == 'test@test.com'


def test_login(client):
	user = User('test@test.com', 'password')
	app.users[user.id] = user
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json()['id'] == user.id
	assert response.get_json()['email'] == 'test@test.com'


def test_create_chat(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
	assert response.get_json()['name'] == 'Test Chat'


def test_send_message(client):
	chat = Chat('Test Chat')
	app.chats[chat.id] = chat
	response = client.post(f'/chat/{chat.id}/message', json={'user_id': '1', 'content': 'Hello, World!'})
	assert response.status_code == 201
	assert 'id' in response.get_json()
	assert response.get_json()['user_id'] == '1'
	assert response.get_json()['content'] == 'Hello, World!'
