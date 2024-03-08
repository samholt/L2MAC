import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'name': 'Test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_logout(client):
	response = client.post('/logout')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out successfully'}


def test_update_profile(client):
	response = client.post('/update_profile', json={'email': 'test@test.com', 'password': 'test123', 'profile_picture': 'test.jpg', 'status_message': 'Hello, world!', 'privacy_settings': {'last_seen': 'everyone'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}
