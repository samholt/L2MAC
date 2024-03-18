import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_post_status(client):
	app.users_db['test@test.com'] = {'email': 'test@test.com', 'password': 'test', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': [], 'groups': {}, 'messages': []}
	response = client.post('/post_status', json={'email': 'test@test.com', 'status': 'Hello, world!', 'visibility': ['friend@test.com']})
	assert response.status_code == 200
	assert app.users_db['test@test.com']['status'] == 'Hello, world!'
	assert app.users_db['test@test.com']['visibility'] == ['friend@test.com']


def test_manage_visibility(client):
	app.users_db['test@test.com'] = {'email': 'test@test.com', 'password': 'test', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': [], 'groups': {}, 'messages': []}
	response = client.post('/manage_visibility', json={'email': 'test@test.com', 'visibility': ['friend@test.com', 'another_friend@test.com']})
	assert response.status_code == 200
	assert app.users_db['test@test.com']['visibility'] == ['friend@test.com', 'another_friend@test.com']


def test_update_online_status(client):
	app.users_db['test@test.com'] = {'email': 'test@test.com', 'password': 'test', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': [], 'groups': {}, 'messages': []}
	response = client.post('/online_status', json={'email': 'test@test.com', 'status': 'offline'})
	assert response.status_code == 200
	assert app.users_db['test@test.com']['online'] == 'offline'
	response = client.post('/online_status', json={'email': 'test@test.com', 'status': 'online'})
	assert response.status_code == 200
	assert app.users_db['test@test.com']['online'] == 'online'

# Existing tests...


