import pytest
import app
from user import User
from chat import Chat
from message import Message

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	data = response.get_json()
	return data['id']


def test_register(client):
	response = client.post('/register', json={'email': 'test2@test.com', 'password': 'password'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['email'] == 'test2@test.com'


def test_login(client, user):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	data = response.get_json()
	assert data['id'] == user
	assert data['email'] == 'test@test.com'


def test_create_chat(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['name'] == 'Test Chat'
	assert data['messages'] == []


def test_send_message(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	data = response.get_json()
	chat_id = data['id']
	response = client.post(f'/chat/{chat_id}/message', json={'user_id': '1', 'content': 'Hello, world!'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['user_id'] == '1'
	assert data['content'] == 'Hello, world!'
	response = client.get(f'/chat/{chat_id}')
	data = response.get_json()
	assert len(data['messages']) == 1
