import pytest
import app
import time

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

# Existing tests...

def test_register(client):
	response = client.get('/user')
	assert response.status_code == 200
	assert b'Register' in response.data

	response = client.post('/user', data={'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert b'Post Status' in response.data

def test_post_status(client):
	response = client.get('/status')
	assert response.status_code == 200
	assert b'Post Status' in response.data

	response = client.post('/status', data={'email': 'test@test.com', 'content': 'Test Status', 'visibility': 'public'})
	assert response.status_code == 200
	assert b'Manage Visibility' in response.data

def test_manage_visibility(client):
	response = client.get('/status/visibility')
	assert response.status_code == 200
	assert b'Manage Visibility' in response.data

	response = client.post('/status/visibility', data={'email': 'test@test.com', 'status_id': '1', 'visibility': 'private'})
	assert response.status_code == 200
	assert 'Status not found' in response.get_data(as_text=True)

# New tests...

def test_check_online(client):
	response = client.get('/check_online', query_string={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'Online'

	# Simulate the user being offline for 5 minutes
	app.users_db['test@test.com']['last_activity'] = time.time() - 300

	response = client.get('/check_online', query_string={'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'Offline'

def test_send_message(client):
	# Check if the user is online or offline
	response = client.get('/check_online', query_string={'email': 'test@test.com'})
	is_online = response.get_data(as_text=True) == 'Online'

	response = client.post('/send_message', data={'email': 'test@test.com', 'message': 'Test Message'})
	assert response.status_code == 200
	assert response.get_data(as_text=True) == 'Message sent'

	if is_online:
		assert 'Test Message' in app.users_db['test@test.com']['messages']
	else:
		assert 'Test Message' in app.users_db['test@test.com']['queue']

def test_receive_messages(client):
	# Add a message to the queue
	app.users_db['test@test.com']['queue'].append('Queued Message')

	response = client.get('/receive_messages', query_string={'email': 'test@test.com'})
	assert response.status_code == 200
	assert 'Queued Message' in response.get_json()['messages']
	assert not app.users_db['test@test.com']['queue']
