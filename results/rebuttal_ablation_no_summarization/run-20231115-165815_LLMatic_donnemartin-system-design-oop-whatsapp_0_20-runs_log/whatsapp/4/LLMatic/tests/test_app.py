import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test'})
	assert response.get_json()['success'] == True


def test_authenticate(client):
	response = client.post('/authenticate', json={'email': 'test@test.com', 'password': 'test'})
	assert response.get_json()['success'] == True


def test_set_profile(client):
	response = client.post('/set_profile', json={'email': 'test@test.com', 'picture': 'test.jpg', 'status': 'Hello'})
	assert response.get_json()['success'] == True


def test_set_privacy(client):
	response = client.post('/set_privacy', json={'email': 'test@test.com', 'privacy': 'private'})
	assert response.get_json()['success'] == True


def test_block_contact(client):
	response = client.post('/register', json={'email': 'contact@test.com', 'password': 'test'})
	assert response.get_json()['success'] == True
	response = client.post('/block_contact', json={'email': 'test@test.com', 'contact': 'contact@test.com'})
	assert response.get_json()['success'] == True


def test_unblock_contact(client):
	response = client.post('/unblock_contact', json={'email': 'test@test.com', 'contact': 'contact@test.com'})
	assert response.get_json()['success'] == True


def test_send_message(client):
	response = client.post('/send_message', json={'id': '1', 'sender': 'test@test.com', 'receiver': 'contact@test.com', 'content': 'Hello'})
	assert response.get_json()['success'] == True


def test_receive_message(client):
	response = client.get('/receive_message/1')
	assert 'message' in response.get_json()


def test_set_read_receipt(client):
	response = client.post('/set_read_receipt', json={'id': '1'})
	assert response.get_json()['success'] == True


def test_encrypt_message(client):
	response = client.post('/encrypt_message', json={'id': '1'})
	assert response.get_json()['success'] == True


def test_share_image(client):
	response = client.post('/share_image', json={'id': '1', 'image': 'image.jpg'})
	assert response.get_json()['success'] == True


def test_create_group(client):
	response = client.post('/create_group', json={'group_id': '1', 'group_name': 'Test Group'})
	assert 'group' in response.get_json()


def test_add_participant(client):
	response = client.post('/add_participant', json={'group_id': '1', 'user_id': 'test@test.com'})
	assert 'group' in response.get_json()


def test_remove_participant(client):
	response = client.post('/remove_participant', json={'group_id': '1', 'user_id': 'test@test.com'})
	assert 'group' in response.get_json()


def test_set_admin(client):
	response = client.post('/set_admin', json={'group_id': '1', 'user_id': 'test@test.com'})
	assert 'group' in response.get_json()


def test_post_status(client):
	response = client.post('/post_status', json={'id': '1', 'user': 'test@test.com', 'image': 'status.jpg', 'visibility': 'public', 'time_limit': '24'})
	assert 'status' in response.get_json()


def test_set_visibility(client):
	response = client.post('/set_visibility', json={'id': '1', 'visibility': 'private'})
	assert 'status' in response.get_json()


def test_set_time_limit(client):
	response = client.post('/set_time_limit', json={'id': '1', 'time_limit': '12'})
	assert 'status' in response.get_json()

