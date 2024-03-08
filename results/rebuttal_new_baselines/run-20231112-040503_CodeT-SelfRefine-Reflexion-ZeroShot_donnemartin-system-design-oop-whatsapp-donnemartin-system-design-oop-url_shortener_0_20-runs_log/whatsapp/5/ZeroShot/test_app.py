import pytest
import json
from app import app, User, users

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return User('Test User', 'test@example.com', 'password')

def test_signup(client, user):
	response = client.post('/signup', data=json.dumps(user.__dict__), content_type='application/json')
	assert response.status_code == 201
	assert users.get(user.email) == user

def test_login(client, user):
	users[user.email] = user
	response = client.post('/login', data=json.dumps({'email': user.email, 'password': user.password}), content_type='application/json')
	assert response.status_code == 200

def test_logout(client, user):
	users[user.email] = user
	response = client.post('/logout', data=json.dumps({'email': user.email}), content_type='application/json')
	assert response.status_code == 200

def test_forgot_password(client, user):
	users[user.email] = user
	response = client.post('/forgot_password', data=json.dumps({'email': user.email}), content_type='application/json')
	assert response.status_code == 200
	assert users.get(user.email).password == 'new_password'
