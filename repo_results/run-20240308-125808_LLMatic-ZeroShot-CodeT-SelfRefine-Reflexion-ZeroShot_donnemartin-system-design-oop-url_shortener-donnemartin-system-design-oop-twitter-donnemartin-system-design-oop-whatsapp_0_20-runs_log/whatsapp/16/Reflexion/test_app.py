import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Test user registration
@pytest.mark.parametrize('name, email, password', [('Test User', 'test@example.com', 'password')])
def test_register(client, name, email, password):
	response = client.post('/register', json={'name': name, 'email': email, 'password': password})
	assert response.status_code == 201
	assert json.loads(response.data)['message'] == 'User registered successfully'

# Test blocking a user
@pytest.mark.parametrize('user_email, blocked_user_email', [('test@example.com', 'blocked@example.com')])
def test_block(client, user_email, blocked_user_email):
	response = client.post('/block', json={'user_email': user_email, 'blocked_user_email': blocked_user_email})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User blocked successfully'

# Test unblocking a user
@pytest.mark.parametrize('user_email, blocked_user_email', [('test@example.com', 'blocked@example.com')])
def test_unblock(client, user_email, blocked_user_email):
	response = client.post('/unblock', json={'user_email': user_email, 'blocked_user_email': blocked_user_email})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'User unblocked successfully'
