import pytest
from app import app, users_db

@pytest.fixture

def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

@pytest.fixture(autouse=True)
def setup():
	users_db['test@example.com'] = {'email': 'test@example.com', 'status': '', 'status_visibility': []}

def test_set_status(client):
	response = client.post('/users/test@example.com/status', json={'status': 'Hello, world!', 'visibility': ['friend1@example.com', 'friend2@example.com']})
	assert response.status_code == 200
	assert users_db['test@example.com']['status'] == 'Hello, world!'
	assert users_db['test@example.com']['status_visibility'] == ['friend1@example.com', 'friend2@example.com']

def test_set_status_visibility(client):
	response = client.post('/users/test@example.com/status/visibility', json={'visibility': ['friend1@example.com']})
	assert response.status_code == 200
	assert users_db['test@example.com']['status_visibility'] == ['friend1@example.com']
