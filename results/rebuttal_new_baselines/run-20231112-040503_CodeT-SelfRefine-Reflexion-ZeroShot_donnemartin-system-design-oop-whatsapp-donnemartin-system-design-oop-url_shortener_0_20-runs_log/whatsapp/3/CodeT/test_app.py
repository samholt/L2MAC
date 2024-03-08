import pytest
import json
from app import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password', 'profile_picture': '', 'status_message': '', 'privacy_settings': {}, 'contacts': [], 'blocked_contacts': [], 'groups': [], 'messages': [], 'status': []})
	assert response.status_code == 201
	assert json.loads(response.data) == {'message': 'User created successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged in successfully'}


def test_logout(client):
	response = client.post('/logout', json={'email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Logged out successfully'}


def test_forgot_password(client):
	response = client.post('/forgot_password', json={'email': 'test@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Password reset successfully'}


def test_set_profile_picture(client):
	response = client.post('/set_profile_picture', json={'email': 'test@example.com', 'profile_picture': 'new_picture.jpg'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Profile picture set successfully'}


def test_set_status_message(client):
	response = client.post('/set_status_message', json={'email': 'test@example.com', 'status_message': 'Hello, world!'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Status message set successfully'}


def test_set_privacy_settings(client):
	response = client.post('/set_privacy_settings', json={'email': 'test@example.com', 'privacy_settings': {'last_seen': 'everyone'}})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Privacy settings set successfully'}


def test_block_contact(client):
	response = client.post('/block_contact', json={'email': 'test@example.com', 'contact_email': 'contact@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Contact blocked successfully'}


def test_unblock_contact(client):
	response = client.post('/unblock_contact', json={'email': 'test@example.com', 'contact_email': 'contact@example.com'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Contact unblocked successfully'}


def test_create_group(client):
	response = client.post('/create_group', json={'email': 'test@example.com', 'group_name': 'Test Group'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Group created successfully'}


def test_edit_group(client):
	response = client.post('/edit_group', json={'email': 'test@example.com', 'old_group_name': 'Test Group', 'new_group_name': 'New Test Group'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Group edited successfully'}


def test_delete_group(client):
	response = client.post('/delete_group', json={'email': 'test@example.com', 'group_name': 'New Test Group'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Group deleted successfully'}


def test_send_message(client):
	response = client.post('/send_message', json={'email': 'test@example.com', 'message': 'Hello, world!'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Message sent successfully'}


def test_read_message(client):
	response = client.post('/read_message', json={'email': 'test@example.com', 'message_index': 0})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Hello, world!'}


def test_post_status(client):
	response = client.post('/post_status', json={'email': 'test@example.com', 'status': 'Hello, world!'})
	assert response.status_code == 200
	assert json.loads(response.data) == {'message': 'Status posted successfully'}


def test_view_status(client):
	response = client.post('/view_status', json={'email': 'test@example.com', 'status_index': 0})
	assert response.status_code == 200
	assert json.loads(response.data) == {'status': 'Hello, world!'}
