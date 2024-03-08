import pytest
import app
import uuid

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['email'] == 'test@test.com'


def test_login(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	data = response.get_json()
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	data = response.get_json()
	assert 'id' in data
	assert data['email'] == 'test@test.com'


def test_create_chat(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['name'] == 'Test Chat'
	assert data['messages'] == []


def test_send_message(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	user_data = response.get_json()
	response = client.post('/chat', json={'name': 'Test Chat'})
	chat_data = response.get_json()
	response = client.post(f'/chat/{chat_data['id']}/message', json={'user_id': user_data['id'], 'content': 'Hello, world!'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['user_id'] == user_data['id']
	assert data['content'] == 'Hello, world!'
