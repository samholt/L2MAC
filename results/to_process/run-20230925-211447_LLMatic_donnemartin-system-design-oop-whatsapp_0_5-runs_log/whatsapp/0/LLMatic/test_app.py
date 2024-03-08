import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'email': 'test@example.com', 'password': 'password'})
	assert response.data == b'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.data == b'Login successful'


def test_reset_password(client):
	response = client.post('/reset_password', json={'token': 'invalid_token', 'new_password': 'new_password'})
	assert response.data == b'Invalid token'


def test_set_profile_picture(client):
	response = client.post('/profile/picture', json={'email': 'test@example.com', 'picture': 'picture.jpg'})
	assert response.data == b'Profile picture updated'


def test_set_status_message(client):
	response = client.post('/profile/status', json={'email': 'test@example.com', 'status': 'Hello, world!'})
	assert response.data == b'Status message updated'


def test_set_privacy_settings(client):
	response = client.post('/profile/privacy', json={'email': 'test@example.com', 'privacy': 'private'})
	assert response.data == b'Privacy settings updated'


def test_block_unblock_contact(client):
	response = client.post('/contacts/block', json={'user_email': 'test@example.com', 'contact_email': 'contact@example.com'})
	assert response.data == b'Contact block status updated'


def test_manage_group(client):
	response = client.post('/contacts/group', json={'user_email': 'test@example.com', 'group_name': 'Friends', 'emails': ['friend1@example.com', 'friend2@example.com']})
	assert response.data == b'Group updated'


def test_send_message(client):
	response = client.post('/messaging/send', json={'sender_email': 'test@example.com', 'receiver_email': 'receiver@example.com', 'message': 'Hello, world!'})
	assert response.data == b'Message sent'


def test_read_message(client):
	response = client.post('/messaging/read', json={'sender_email': 'test@example.com', 'receiver_email': 'receiver@example.com', 'message_id': 0})
	assert response.data == b'Message read'


def test_create_group_chat(client):
	response = client.post('/messaging/group', json={'user_email': 'test@example.com', 'group_name': 'Friends', 'picture': 'group.jpg', 'emails': ['friend1@example.com', 'friend2@example.com']})
	assert response.data == b'Group chat created'


def test_post_status(client):
	response = client.post('/status/post', json={'email': 'test@example.com', 'image': 'status.jpg', 'visibility': ['friend1@example.com', 'friend2@example.com']})
	assert b'-' in response.data


def test_update_visibility(client):
	response = client.post('/status/update_visibility', json={'email': 'test@example.com', 'status_id': 'invalid_id', 'visibility_emails': ['friend1@example.com', 'friend2@example.com']})
	assert response.data == b'False'
