import pytest
import app
from user import User
from contact import Contact
from message import Message
from group_chat import GroupChat
from status import Status

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User registered successfully'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User logged in successfully'}


def test_update_profile(client):
	response = client.put('/profile', json={'email': 'test@test.com', 'picture': 'test.png', 'status_message': 'Hello, world!', 'privacy_settings': 'public'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}


def test_manage_contact(client):
	response = client.post('/contact', json={'email': 'test@test.com', 'contact_email': 'contact@test.com', 'action': 'block'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Contact managed successfully'}


def test_send_message(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'test123'})
	assert response.status_code == 201
	response = client.post('/register', json={'email': 'contact@test.com', 'password': 'test123'})
	assert response.status_code == 201
	response = client.post('/message', json={'email': 'test@test.com', 'receiver_email': 'contact@test.com', 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent successfully'}


def test_manage_group(client):
	response = client.post('/group', json={'email': 'test@test.com', 'name': 'Test Group', 'picture': 'group.png', 'participant_email': 'participant@test.com', 'action': 'add'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Group managed successfully'}


def test_post_status(client):
	response = client.post('/status', json={'email': 'test@test.com', 'image': 'status.png', 'visibility': 'public'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status posted successfully'}
