import pytest
import app
import json
from flask import Flask

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', data=json.dumps({'username': 'test', 'email': 'test@test.com', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Registered successfully' in response.data


def test_login(client):
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'token' in response.data


def test_login_already_logged_in(client):
	client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert b'User already logged in' in response.data


def test_logout(client):
	client.post('/login', data=json.dumps({'username': 'test', 'password': 'test'}), content_type='application/json')
	response = client.post('/logout', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Logged out successfully' in response.data


def test_logout_not_logged_in(client):
	response = client.post('/logout', data=json.dumps({'username': 'test'}), content_type='application/json')
	assert response.status_code == 400
	assert b'User not logged in' in response.data
