import pytest
import app
import json
import hashlib

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_update_status(client):
	response = client.post('/user', data=json.dumps({'email': 'test1@test.com', 'password': 'test'}), content_type='application/json')
	response = client.post('/user/status', data=json.dumps({'email': 'test1@test.com', 'status': 'offline'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Status updated successfully' in response.data


def test_send_message(client):
	response = client.post('/user', data=json.dumps({'email': 'test2@test.com', 'password': 'test'}), content_type='application/json')
	response = client.post('/message/send', data=json.dumps({'sender': 'test1@test.com', 'receiver': 'test2@test.com', 'message': 'Hello'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Message sent successfully' in response.data


def test_receive_message(client):
	response = client.post('/user/status', data=json.dumps({'email': 'test2@test.com', 'status': 'online'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Status updated successfully' in response.data
	response = client.get('/user/test2@test.com')
	data = json.loads(response.data)
	assert len(data['messages']) == 1
	assert data['messages'][0]['message'] == hashlib.sha256('Hello'.encode()).hexdigest()


def test_offline_message_queue(client):
	response = client.post('/user', data=json.dumps({'email': 'test3@test.com', 'password': 'test'}), content_type='application/json')
	response = client.post('/user/status', data=json.dumps({'email': 'test3@test.com', 'status': 'offline'}), content_type='application/json')
	response = client.post('/message/send', data=json.dumps({'sender': 'test1@test.com', 'receiver': 'test3@test.com', 'message': 'Hello'}), content_type='application/json')
	assert response.status_code == 200
	assert b'Message sent successfully' in response.data
	response = client.get('/user/test3@test.com')
	data = json.loads(response.data)
	assert len(data['queue']) == 1
	assert data['queue'][0]['message'] == hashlib.sha256('Hello'.encode()).hexdigest()
