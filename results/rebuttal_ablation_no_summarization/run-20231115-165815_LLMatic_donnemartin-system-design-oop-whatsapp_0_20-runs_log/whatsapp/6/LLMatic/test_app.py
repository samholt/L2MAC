import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		client.post('/users', json={'email': 'test@example.com', 'password': 'testpass', 'profile_picture': '', 'status': '', 'status_visibility': [], 'privacy_settings': {}, 'blocked_contacts': [], 'groups': {}, 'messages': [], 'online_status': 'online', 'message_queue': []})
		client.post('/users', json={'email': 'receiver@example.com', 'password': 'receiverpass', 'profile_picture': '', 'status': '', 'status_visibility': [], 'privacy_settings': {}, 'blocked_contacts': [], 'groups': {}, 'messages': [], 'online_status': 'online', 'message_queue': []})
		yield client


def test_create_user(client):
	response = client.post('/users', json={'email': 'newuser@example.com', 'password': 'newpass', 'profile_picture': '', 'status': '', 'status_visibility': [], 'privacy_settings': {}, 'blocked_contacts': [], 'groups': {}, 'messages': [], 'online_status': 'online', 'message_queue': []})
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created'}


def test_get_user(client):
	response = client.get('/users/test@example.com')
	assert response.status_code == 200
	assert response.get_json() == {'email': 'test@example.com', 'password': 'testpass', 'profile_picture': '', 'status': '', 'status_visibility': [], 'privacy_settings': {}, 'blocked_contacts': [], 'groups': {}, 'messages': [], 'online_status': 'online', 'message_queue': []}


def test_recover_password(client):
	response = client.post('/users/test@example.com/recover')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Password recovery email sent'}


def test_set_profile_picture(client):
	response = client.post('/users/test@example.com/profile_picture', json={'profile_picture': 'new_picture.jpg'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile picture updated'}


def test_set_status(client):
	response = client.post('/users/test@example.com/status', json={'status': 'Hello, world!', 'visibility': ['friend1@example.com', 'friend2@example.com']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status updated'}


def test_set_status_visibility(client):
	response = client.post('/users/test@example.com/status/visibility', json={'visibility': ['friend1@example.com']})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Status visibility updated'}


def test_set_online_status(client):
	response = client.post('/users/test@example.com/online_status', json={'online_status': 'offline'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Online status updated'}


def test_send_message(client):
	response = client.post('/users/test@example.com/send_message', json={'receiver_email': 'receiver@example.com', 'message': 'Hello, receiver!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message sent'}


def test_send_message_offline(client):
	client.post('/users/receiver@example.com/online_status', json={'online_status': 'offline'})
	response = client.post('/users/test@example.com/send_message', json={'receiver_email': 'receiver@example.com', 'message': 'Hello, receiver!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Message queued'}

# Rest of the tests...
