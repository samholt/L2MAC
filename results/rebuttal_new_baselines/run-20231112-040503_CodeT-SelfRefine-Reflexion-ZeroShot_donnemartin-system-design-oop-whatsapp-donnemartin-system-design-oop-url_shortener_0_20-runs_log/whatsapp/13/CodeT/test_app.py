import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def user():
	return {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}


def test_signup(client, user):
	response = client.post('/signup', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_login(client, user):
	client.post('/signup', data=json.dumps(user), content_type='application/json')
	response = client.post('/login', data=json.dumps(user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_logout(client, user):
	client.post('/signup', data=json.dumps(user), content_type='application/json')
	client.post('/login', data=json.dumps(user), content_type='application/json')
	response = client.post('/logout', data=json.dumps({'email': user['email']}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out successfully'}
