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
	assert response.get_json()['message'] == 'User registered successfully'

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_login(client, email, password):
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Login successful'

@pytest.mark.parametrize('email,old_password,new_password', [('test@test.com', 'password', 'new_password')])
def test_reset_password(client, email, old_password, new_password):
	response = client.post('/reset_password', json={'email': email, 'old_password': old_password, 'new_password': new_password})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Password reset successful'
