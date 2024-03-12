import pytest
import app
import hashlib
import time

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Existing tests...

def test_register(client):
	response = client.post('/register', json={'username': 'user@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}
	assert 'user@test.com' in app.users_db
	assert app.users_db['user@test.com']['password'] == hashlib.sha256('password'.encode()).hexdigest()
	assert app.users_db['user@test.com']['status'] == 'offline'
	assert app.users_db['user@test.com']['queue'] == []

def test_login(client):
	app.users_db['user@test.com'] = {'password': hashlib.sha256('password'.encode()).hexdigest(), 'contacts': [], 'status': 'offline', 'queue': []}
	response = client.post('/login', json={'username': 'user@test.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User logged in successfully'}
	assert app.users_db['user@test.com']['status'] == 'online'

def test_logout(client):
	app.users_db['user@test.com'] = {'password': hashlib.sha256('password'.encode()).hexdigest(), 'contacts': [], 'status': 'online', 'queue': []}
	response = client.post('/logout', json={'username': 'user@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User logged out successfully'}
	assert app.users_db['user@test.com']['status'] == 'offline'

def test_send_message(client):
	app.users_db['user@test.com'] = {'password': hashlib.sha256('password'.encode()).hexdigest(), 'contacts': [], 'status': 'online', 'queue': []}
	app.users_db['contact@test.com'] = {'password': hashlib.sha256('password'.encode()).hexdigest(), 'contacts': [], 'status': 'offline', 'queue': []}
	response = client.post('/message', json={'sender': 'user@test.com', 'receiver': 'contact@test.com', 'message': 'Hello, Contact!'})
	assert response.status_code == 200
	assert 'message_id' in response.get_json()
	assert response.get_json()['message'] == 'Message queued'
	assert response.get_json()['message_id'] not in app.messages_db
	assert app.users_db['contact@test.com']['queue'] != []

	app.users_db['contact@test.com']['status'] = 'online'
	response = client.post('/message', json={'sender': 'user@test.com', 'receiver': 'contact@test.com', 'message': 'Hello, Contact!'})
	assert response.status_code == 200
	assert 'message_id' in response.get_json()
	assert response.get_json()['message'] == 'Message sent successfully'
	assert response.get_json()['message_id'] in app.messages_db
	assert app.messages_db[response.get_json()['message_id']]['sender'] == 'user@test.com'
	assert app.messages_db[response.get_json()['message_id']]['receiver'] == 'contact@test.com'
	assert app.messages_db[response.get_json()['message_id']]['message'] == 'Hello, Contact!'

