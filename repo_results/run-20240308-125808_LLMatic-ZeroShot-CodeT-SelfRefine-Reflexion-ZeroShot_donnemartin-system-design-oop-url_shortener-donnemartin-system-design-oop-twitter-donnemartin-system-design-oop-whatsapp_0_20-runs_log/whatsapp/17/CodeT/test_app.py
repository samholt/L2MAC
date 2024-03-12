import pytest
import json
from app import app, User, Message, users, messages

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture
def sample_user():
	return User('Test User', 'test@example.com', 'password')

@pytest.fixture
def sample_message(sample_user):
	return Message(sample_user.email, 'recipient@example.com', 'Hello, World!')


def test_register(client, sample_user):
	response = client.post('/register', data=json.dumps(sample_user.__dict__), content_type='application/json')
	assert response.status_code == 201
	assert users[sample_user.email] == sample_user


def test_login(client, sample_user):
	users[sample_user.email] = sample_user
	response = client.post('/login', data=json.dumps({'email': sample_user.email, 'password': sample_user.password}), content_type='application/json')
	assert response.status_code == 200


def test_send_message(client, sample_message):
	response = client.post('/send_message', data=json.dumps(sample_message.__dict__), content_type='application/json')
	assert response.status_code == 201
	assert messages[sample_message.to_user][0] == sample_message


def test_read_messages(client, sample_message):
	messages[sample_message.to_user] = [sample_message]
	response = client.get('/read_messages', query_string={'email': sample_message.to_user})
	assert response.status_code == 200
	assert messages[sample_message.to_user][0].read
