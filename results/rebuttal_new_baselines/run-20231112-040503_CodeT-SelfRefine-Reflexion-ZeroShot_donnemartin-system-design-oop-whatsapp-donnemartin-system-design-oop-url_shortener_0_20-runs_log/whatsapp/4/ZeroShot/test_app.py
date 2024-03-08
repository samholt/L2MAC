import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'User registered'}

	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Email already registered'}

def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'User logged in'}

	response = client.post('/login', json={'email': 'wrong@test.com', 'password': 'test'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid email or password'}

	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrong'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid email or password'}

def test_send_message(client):
	response = client.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 400
	assert json.loads(response.data) == {'error': 'Invalid sender or receiver'}

	response = client.post('/register', json={'email': 'test2@test.com', 'password': 'test2'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'User registered'}

	response = client.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'success': 'Message sent'}

def test_get_messages(client):
	response = client.get('/get_messages?user=test@test.com')
	assert response.status_code == 200
	assert json.loads(response.data) == {'messages': [{'to': 'test2@test.com', 'message': 'Hello'}]}
