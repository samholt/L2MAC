import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'id': '1', 'email': 'test@test.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User registered successfully'}
	response = client.post('/register', json={'id': '1', 'email': 'test@test.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}})
	assert response.status_code == 400
	assert json.loads(response.data) == {'message': 'User already exists'}

def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Login successful'}

def test_forgot_password(client):
	response = client.post('/forgot_password', json={'id': '1', 'new_password': 'new_password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Password updated successfully'}

def test_update_profile(client):
	response = client.post('/update_profile', json={'id': '1', 'profile_picture': 'new_picture', 'status_message': 'new_status', 'privacy_settings': {'last_seen': 'public'}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Profile updated successfully'}

def test_send_message(client):
	response = client.post('/send_message', json={'id': '1', 'from_user': '1', 'to_user': '2', 'content': 'Hello', 'read': False, 'encrypted': False})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'Message sent successfully'}

def test_read_message(client):
	response = client.post('/read_message', json={'id': '1'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Message marked as read'}
