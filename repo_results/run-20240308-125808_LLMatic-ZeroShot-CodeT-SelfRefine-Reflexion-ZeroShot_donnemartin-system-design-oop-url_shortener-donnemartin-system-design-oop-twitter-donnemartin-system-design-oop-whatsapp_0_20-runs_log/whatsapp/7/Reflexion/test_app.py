import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}

def test_register(client, user):
	response = client.post('/register', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client, user):
	client.post('/register', data=json.dumps(user), content_type='application/json')
	response = client.post('/login', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

def test_logout(client, user):
	client.post('/register', data=json.dumps(user), content_type='application/json')
	client.post('/login', data=json.dumps(user), content_type='application/json')
	response = client.post('/logout', data=json.dumps({'email': user['email']}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out successfully'}

def test_forgot_password(client, user):
	client.post('/register', data=json.dumps(user), content_type='application/json')
	response = client.post('/forgot_password', data=json.dumps({'email': user['email']}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password reset link sent to email'}

def test_set_profile_picture(client, user):
	client.post('/register', data=json.dumps(user), content_type='application/json')
	response = client.post('/set_profile_picture', data=json.dumps({'email': user['email'], 'profile_picture': 'picture.jpg'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture set successfully'}

def test_set_status_message(client, user):
	client.post('/register', data=json.dumps(user), content_type='application/json')
	response = client.post('/set_status_message', data=json.dumps({'email': user['email'], 'status_message': 'Hello, world!'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status message set successfully'}

def test_set_privacy_settings(client, user):
	client.post('/register', data=json.dumps(user), content_type='application/json')
	response = client.post('/set_privacy_settings', data=json.dumps({'email': user['email'], 'privacy_settings': {'last_seen': 'everyone', 'profile_picture': 'contacts_only'}}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Privacy settings set successfully'}
