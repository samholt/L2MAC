import pytest
import json
from app import app, User, users, sessions

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 201
	assert 'User created successfully' in response.get_data(as_text=True)
	assert User.query.filter_by(email='test@example.com').first() is not None

	# Test signup with existing email
	response = client.post('/signup', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 400
	assert 'Email already in use' in response.get_data(as_text=True)


def test_login(client):
	# Test login without signup
	response = client.post('/login', data=json.dumps({'email': 'test2@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 404
	assert 'User does not exist' in response.get_data(as_text=True)

	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert 'Logged in successfully' in response.get_data(as_text=True)
	assert 'test@example.com' in sessions


def test_logout(client):
	# Test logout without login
	response = client.post('/logout', data=json.dumps({'email': 'test2@example.com'}), content_type='application/json')
	assert response.status_code == 403
	assert 'User is not logged in' in response.get_data(as_text=True)

	response = client.post('/logout', data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'Logged out successfully' in response.get_data(as_text=True)
	assert 'test@example.com' not in sessions
