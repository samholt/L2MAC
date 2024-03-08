import pytest
from flask import Flask
import app
import uuid

# ... rest of the code remains the same ...

def test_home(client):
	response = client.get('/')
	assert response.status_code == 200
	assert b'Welcome to the application!' in response.data

# ... rest of the code remains the same ...

def test_status(client):
	user_id = str(uuid.uuid4())
	app.users[user_id] = {'status': 'online'}
	response = client.post('/status', json={'user_id': user_id, 'status': 'offline'})
	assert response.status_code == 200
	assert app.users[user_id]['status'] == 'offline'

def test_message(client):
	from_user = str(uuid.uuid4())
	to_user = str(uuid.uuid4())
	message = 'Hello, World!'
	app.users[from_user] = {'status': 'online'}
	app.users[to_user] = {'status': 'offline'}
	response = client.post('/message', json={'from': from_user, 'to': to_user, 'message': message})
	assert response.status_code == 200
	assert app.message_queue[to_user][0]['message'] == message

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client
