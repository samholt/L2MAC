import pytest
from models import User
from database import users
from app import app as flask_app


@pytest.fixture
def app():
	return flask_app


def test_register(client):
	response = client.post('/register', json={'email': 'test@example.com', 'username': 'test', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}
	assert 'test@example.com' in users


def test_login(client):
	user = User('test@example.com', 'test', 'password')
	users[user.email] = user
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_invalid_login(client):
	response = client.post('/login', json={'email': 'invalid@example.com', 'password': 'password'})
	assert response.status_code == 401
	assert response.get_json() == {'error': 'Invalid email or password'}
