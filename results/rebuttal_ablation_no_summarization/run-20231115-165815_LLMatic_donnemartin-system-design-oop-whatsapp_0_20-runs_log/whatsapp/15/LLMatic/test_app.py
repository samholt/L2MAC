import pytest
import app
import time

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/api/users', json={'email': 'test@test.com'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}
	assert 'test@test.com' in app.users_db

def test_update_status(client):
	app.users_db['test@test.com'] = {'messages': [], 'read_receipts': {}, 'status': None, 'status_visibility': [], 'contacts': [], 'message_queue': []}
	response = client.post('/api/update_status', json={'email': 'test@test.com', 'status': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status updated'}
	assert app.users_db['test@test.com']['status'] == 'Hello, world!'

def test_add_contact(client):
	app.users_db['test1@test.com'] = {'messages': [], 'read_receipts': {}, 'status': None, 'status_visibility': [], 'contacts': [], 'message_queue': []}
	response = client.post('/api/add_contact', json={'email': 'test@test.com', 'contact_email': 'test1@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact added'}
	assert 'test1@test.com' in app.users_db['test@test.com']['contacts']

def test_send_message(client):
	app.users_db['test1@test.com'] = {'messages': [], 'read_receipts': {}, 'status': 'offline', 'status_visibility': [], 'contacts': [], 'message_queue': []}
	response = client.post('/api/send_message', json={'from_email': 'test@test.com', 'to_email': 'test1@test.com', 'message': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent'}
	assert any(message['from'] == 'test@test.com' and message['to'] == 'test1@test.com' and message['message'] == 'Hello, world!' for message in app.users_db['test1@test.com']['message_queue'])

def test_create_group(client):
	app.users_db['test1@test.com'] = {'messages': [], 'read_receipts': {}, 'status': None, 'status_visibility': [], 'contacts': [], 'message_queue': []}
	response = client.post('/api/create_group', json={'group_name': 'test_group', 'emails': ['test@test.com', 'test1@test.com']})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'Group created'}
	assert 'test_group' in app.groups_db
	assert app.groups_db['test_group']['members'] == ['test@test.com', 'test1@test.com']
	assert app.groups_db['test_group']['admins'] == ['test@test.com']

def test_update_status_visibility(client):
	app.users_db['test1@test.com'] = {'messages': [], 'read_receipts': {}, 'status': None, 'status_visibility': [], 'contacts': [], 'message_queue': []}
	response = client.post('/api/update_status_visibility', json={'email': 'test@test.com', 'status_visibility': ['test1@test.com']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status visibility updated'}
	assert app.users_db['test@test.com']['status_visibility'] == ['test1@test.com']

