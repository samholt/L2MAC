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
	response = client.post('/register', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Registration successful'

	response = client.post('/register', json={'email': email, 'password': password})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Email already in use'

@pytest.mark.parametrize('email,password', [('test@test.com', 'password')])
def test_login(client, email, password):
	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid email or password'

	client.post('/register', json={'email': email, 'password': password})

	response = client.post('/login', json={'email': email, 'password': password})
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Login successful'
