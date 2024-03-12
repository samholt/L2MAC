import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_online_status(client):
	response = client.post('/signup', json={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 201
	response = client.post('/online_status', json={'email': 'test@test.com', 'status': False})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Online status updated successfully'
	assert app.users['test@test.com']['online'] == False


def test_send_message(client):
	response = client.post('/signup', json={'email': 'test1@test.com', 'password': 'test'})
	assert response.status_code == 201
	response = client.post('/signup', json={'email': 'test2@test.com', 'password': 'test'})
	assert response.status_code == 201
	response = client.post('/online_status', json={'email': 'test2@test.com', 'status': False})
	assert response.status_code == 200
	response = client.post('/send_message', json={'sender_email': 'test1@test.com', 'receiver_email': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 200
	assert json.loads(response.data)['message'] == 'Message queued successfully'
	assert ('test1@test.com', 'Hello') in app.offline_messages['test2@test.com']
