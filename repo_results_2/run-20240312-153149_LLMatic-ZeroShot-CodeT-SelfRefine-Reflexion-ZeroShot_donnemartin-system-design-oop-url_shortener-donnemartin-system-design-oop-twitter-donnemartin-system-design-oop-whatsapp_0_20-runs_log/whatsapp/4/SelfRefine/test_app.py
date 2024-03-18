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

@pytest.fixture
def sample_message(sample_user):
	return {
		'from_user': sample_user['email'],
		'to_user': 'another@example.com',
		'message': 'Hello, World!'
	}


def test_register(client, sample_user):
	response = client.post('/register', data=json.dumps(sample_user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['status'] == 'success'


def test_login(client, sample_user):
	client.post('/register', data=json.dumps(sample_user), content_type='application/json')
	response = client.post('/login', data=json.dumps(sample_user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['status'] == 'success'


def test_message(client, sample_user, sample_message):
	client.post('/register', data=json.dumps(sample_user), content_type='application/json')
	response = client.post('/message', data=json.dumps(sample_message), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['status'] == 'success'
