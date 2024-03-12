import pytest
import json
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_signup(client):
	response = client.post('/signup', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'contacts': [], 'blocked_contacts': [], 'groups': [], 'messages': [], 'status': []}), content_type='application/json')
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}

def test_login(client):
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}

def test_logout(client):
	response = client.post('/logout', data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged out successfully'}

def test_forgot_password(client):
	response = client.post('/forgot_password', data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Password reset link sent to your email'}
