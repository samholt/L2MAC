import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_register(client, email, password):
	response = client.post('/register', json={'name': 'Test User', 'email': email, 'password': password})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_login(client, email, password):
	client.post('/register', json={'name': 'Test User', 'email': email, 'password': password})
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_update_profile(client, email, password):
	client.post('/register', json={'name': 'Test User', 'email': email, 'password': password})
	client.post('/login', json={'email': email, 'password': password})
	response = client.put('/profile', json={'email': email, 'profile_picture': 'picture.jpg', 'status_message': 'Hello'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}
