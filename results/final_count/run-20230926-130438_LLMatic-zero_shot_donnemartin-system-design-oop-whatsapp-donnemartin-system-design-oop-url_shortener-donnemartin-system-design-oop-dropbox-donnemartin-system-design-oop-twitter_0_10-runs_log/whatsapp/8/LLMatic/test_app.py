import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.data == b'User created'


def test_home(client):
	response = client.get('/')
	assert response.status_code == 200


def test_profile(client):
	response = client.get('/profile')
	assert response.status_code == 200


def test_contacts(client):
	response = client.get('/contacts')
	assert response.status_code == 200


def test_messages(client):
	response = client.get('/messages')
	assert response.status_code == 200


def test_groups(client):
	response = client.get('/groups')
	assert response.status_code == 200


def test_statuses(client):
	response = client.get('/statuses')
	assert response.status_code == 200


def test_online(client):
	response = client.post('/online', json={'user': 'test@test.com', 'status': True})
	assert response.status_code == 200
	assert response.data == b'Status updated'
	assert app.DATABASE['users']['test@test.com']['online'] == True


def test_message_queue(client):
	response = client.post('/signup', json={'email': 'test2@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.data == b'User created'
	response = client.post('/online', json={'user': 'test@test.com', 'status': False})
	assert response.status_code == 200
	assert response.data == b'Status updated'
	assert app.DATABASE['users']['test@test.com']['online'] == False
	response = client.post('/messages', json={'sender': 'test2@test.com', 'receiver': 'test@test.com', 'message': 'Hello'})
	assert response.status_code == 201
	assert response.data == b'Message sent'
	assert app.DATABASE['message_queue']['test@test.com'] == [{'sender': 'test2@test.com', 'message': 'Hello'}]
	response = client.post('/online', json={'user': 'test@test.com', 'status': True})
	assert response.status_code == 200
	assert response.data == b'Status updated'
	assert app.DATABASE['users']['test@test.com']['online'] == True
	assert app.DATABASE['messages']['test@test.com'] == {'sender': 'test2@test.com', 'message': 'Hello'}
	assert app.DATABASE['message_queue']['test@test.com'] == []
