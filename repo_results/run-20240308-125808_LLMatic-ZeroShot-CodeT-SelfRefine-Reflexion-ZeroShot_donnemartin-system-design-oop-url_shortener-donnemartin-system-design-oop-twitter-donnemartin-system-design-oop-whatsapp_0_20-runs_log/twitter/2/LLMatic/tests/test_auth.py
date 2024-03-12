import pytest
from flask import json
from models import User


def test_registration(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'User registered successfully'

def test_auth(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

def test_invalid_auth(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'wrongpassword'})
	assert response.status_code == 400
