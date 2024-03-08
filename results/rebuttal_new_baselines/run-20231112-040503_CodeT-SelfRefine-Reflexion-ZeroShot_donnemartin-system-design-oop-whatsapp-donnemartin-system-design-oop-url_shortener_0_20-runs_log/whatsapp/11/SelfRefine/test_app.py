import pytest
import json
from app import app, User, Message, db

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}
	assert User.query.filter_by(email='test@test.com').first() is not None

	response = client.post('/register', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Email already in use'}

def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 401
	assert json.loads(response.data) == {'message': 'Invalid email or password'}

def test_send_message(client):
	response = client.post('/send_message', json={'from_user': 'test@test.com', 'to_user': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'Recipient email not found'}

	response = client.post('/register', json={'name': 'Test2', 'email': 'test2@test.com', 'password': 'test2'})
	assert response.status_code == 201

	response = client.post('/send_message', json={'from_user': 'test@test.com', 'to_user': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Message sent successfully'}
	assert Message.query.filter_by(to_user='test2@test.com').first() is not None

def test_read_messages(client):
	response = client.get('/read_messages', query_string={'email': 'test2@test.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'messages': ['Hello']}
	assert all(message.read for message in Message.query.filter_by(to_user='test2@test.com').all())
