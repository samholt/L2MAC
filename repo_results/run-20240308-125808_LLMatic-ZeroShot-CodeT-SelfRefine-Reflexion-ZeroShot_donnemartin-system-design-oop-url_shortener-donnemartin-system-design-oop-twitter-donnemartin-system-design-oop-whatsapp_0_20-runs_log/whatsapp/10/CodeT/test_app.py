import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'id': '1', 'email': 'test@test.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'blocked_contacts': [], 'groups': []})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_login(client):
	response = client.post('/login', json={'id': '1', 'password': 'password'})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_forgot_password(client):
	response = client.post('/forgot_password', json={'id': '1', 'email': 'test@test.com', 'new_password': 'new_password'})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_update_profile(client):
	response = client.post('/update_profile', json={'id': '1', 'profile_picture': 'new_picture', 'status_message': 'new_status', 'privacy_settings': {'last_seen': 'everyone'}})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_block_contact(client):
	response = client.post('/block_contact', json={'id': '1', 'contact_id': '2'})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_unblock_contact(client):
	response = client.post('/unblock_contact', json={'id': '1', 'contact_id': '2'})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_create_group(client):
	response = client.post('/create_group', json={'id': '1', 'group_id': '1', 'name': 'group', 'picture': ''})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_send_message(client):
	response = client.post('/send_message', json={'id': '1', 'sender': '1', 'receiver': '2', 'content': 'hello', 'read': False, 'encrypted': False})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200

def test_read_message(client):
	response = client.post('/read_message', json={'id': '1', 'user_id': '2'})
	assert response.get_json() == {'status': 'success'}
	assert response.status_code == 200
