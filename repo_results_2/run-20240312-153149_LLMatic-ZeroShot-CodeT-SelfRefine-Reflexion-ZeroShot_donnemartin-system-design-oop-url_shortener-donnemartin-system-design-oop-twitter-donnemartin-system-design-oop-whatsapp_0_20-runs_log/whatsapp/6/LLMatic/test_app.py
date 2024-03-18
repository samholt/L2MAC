import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_home_page(client):
	response = client.get('/')
	assert response.status_code == 200
	assert b'Welcome to Chat App' in response.data


def test_set_status(client):
	response = client.post('/set_status', json={'email': 'test@test.com', 'status': True})
	assert response.status_code == 404
	assert b'Email not found' in response.data

	app.DATABASE['users']['test@test.com'] = {'online': False}
	response = client.post('/set_status', json={'email': 'test@test.com', 'status': True})
	assert response.status_code == 200
	assert b'Status updated' in response.data
	assert app.DATABASE['users']['test@test.com']['online'] == True


def test_send_message(client):
	app.DATABASE['users']['test1@test.com'] = {'online': True}
	app.DATABASE['users']['test2@test.com'] = {'online': False}
	response = client.post('/send_message', json={'sender': 'test1@test.com', 'receiver': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 200
	assert b'Message sent' in response.data
	assert b'queued' in response.data

	app.DATABASE['users']['test2@test.com']['online'] = True
	response = client.post('/send_message', json={'sender': 'test1@test.com', 'receiver': 'test2@test.com', 'message': 'Hello'})
	assert response.status_code == 200
	assert b'Message sent' in response.data
	assert b'sent' in response.data
