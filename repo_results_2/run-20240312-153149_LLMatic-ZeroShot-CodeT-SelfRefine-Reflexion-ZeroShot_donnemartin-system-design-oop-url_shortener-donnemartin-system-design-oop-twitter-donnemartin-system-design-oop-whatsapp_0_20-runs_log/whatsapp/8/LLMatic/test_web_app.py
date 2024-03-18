import pytest
import app

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
	assert b'Status not found' in response.data
