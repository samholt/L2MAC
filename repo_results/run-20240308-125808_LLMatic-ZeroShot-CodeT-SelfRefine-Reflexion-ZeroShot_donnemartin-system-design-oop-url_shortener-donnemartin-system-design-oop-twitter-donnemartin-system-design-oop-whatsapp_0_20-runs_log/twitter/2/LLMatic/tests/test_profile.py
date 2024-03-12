import pytest
from flask import json
from models import User


def test_profile(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

	response = client.post('/profile', json={'email': 'test@test.com', 'profile_picture': 'pic.jpg', 'bio': 'This is a test bio', 'website': 'www.test.com', 'location': 'Test City'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Profile updated successfully'

	response = client.get('/profile', json={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json()['email'] == 'test@test.com'
	assert response.get_json()['username'] == 'test'
	assert response.get_json()['profile_picture'] == 'pic.jpg'
	assert response.get_json()['bio'] == 'This is a test bio'
	assert response.get_json()['website'] == 'www.test.com'
	assert response.get_json()['location'] == 'Test City'

	response = client.post('/profile', json={'email': 'test@test.com', 'private': True})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Profile updated successfully'

	response = client.get('/profile', json={'email': 'test@test.com'})
	assert response.status_code == 403
	assert response.get_json()['error'] == 'This profile is private'
