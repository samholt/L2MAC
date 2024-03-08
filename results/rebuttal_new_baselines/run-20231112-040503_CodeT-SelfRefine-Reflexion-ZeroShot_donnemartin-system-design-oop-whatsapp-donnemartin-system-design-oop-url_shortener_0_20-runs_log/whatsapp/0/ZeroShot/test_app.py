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
	return {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}

@pytest.fixture
def sample_message():
	return {'from_user': 'test@example.com', 'to_user': 'test2@example.com', 'message': 'Hello'}


def test_signup(client, sample_user):
	response = client.post('/signup', data=json.dumps(sample_user), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created'


def test_login(client, sample_user):
	client.post('/signup', data=json.dumps(sample_user), content_type='application/json')
	response = client.post('/login', data=json.dumps(sample_user), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in'


def test_send_message(client, sample_user, sample_message):
	client.post('/signup', data=json.dumps(sample_user), content_type='application/json')
	response = client.post('/message', data=json.dumps(sample_message), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'Message sent'


def test_get_messages(client, sample_user, sample_message):
	client.post('/signup', data=json.dumps(sample_user), content_type='application/json')
	client.post('/message', data=json.dumps(sample_message), content_type='application/json')
	response = client.get('/message?from_user=test@example.com&to_user=test2@example.com')
	assert response.status_code == 200
	assert len(response.get_json()) == 1
