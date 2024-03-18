import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_signup(client, email, password):
	response = client.post('/signup', json={'name': 'Test', 'email': email, 'password': password})
	assert response.status_code == 201
	assert app.users[email].email == email

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_login(client, email, password):
	client.post('/signup', json={'name': 'Test', 'email': email, 'password': password})
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert app.sessions[email] == 'Logged In'

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_logout(client, email, password):
	client.post('/signup', json={'name': 'Test', 'email': email, 'password': password})
	client.post('/login', json={'email': email, 'password': password})
	response = client.post('/logout', json={'email': email})
	assert response.status_code == 200
	assert email not in app.sessions

@pytest.mark.parametrize('email,password,profile_picture,status_message,privacy_settings', [('test@test.com', 'password', 'picture.jpg', 'Hello', {'last_seen': 'everyone'})])
def test_update_profile(client, email, password, profile_picture, status_message, privacy_settings):
	client.post('/signup', json={'name': 'Test', 'email': email, 'password': password})
	client.post('/login', json={'email': email, 'password': password})
	response = client.post('/update_profile', json={'email': email, 'profile_picture': profile_picture, 'status_message': status_message, 'privacy_settings': privacy_settings})
	assert response.status_code == 200
	assert app.users[email].profile_picture == profile_picture
	assert app.users[email].status_message == status_message
	assert app.users[email].privacy_settings == privacy_settings
