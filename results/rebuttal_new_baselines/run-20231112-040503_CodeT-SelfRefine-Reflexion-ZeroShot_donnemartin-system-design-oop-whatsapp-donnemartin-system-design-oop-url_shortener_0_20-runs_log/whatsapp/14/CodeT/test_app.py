import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_user():
	return {
		'name': 'Test User',
		'email': 'test@example.com',
		'password': 'password'
	}


def test_signup(client, sample_user):
	response = client.post('/signup', data=json.dumps(sample_user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}


def test_login(client, sample_user):
	client.post('/signup', data=json.dumps(sample_user), content_type='application/json')
	response = client.post('/login', data=json.dumps(sample_user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_logout(client, sample_user):
	client.post('/signup', data=json.dumps(sample_user), content_type='application/json')
	client.post('/login', data=json.dumps(sample_user), content_type='application/json')
	response = client.post('/logout', data=json.dumps({'email': sample_user['email']}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out successfully'}
