import pytest
from app import app
from user import User
from contact import Contact
from group import Group
from message import Message
from status import Status


@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.get_data() == b'User registered successfully'


def test_login(client):
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.get_data() == b'User logged in successfully'


def test_forgot_password(client):
	response = client.post('/forgot_password', json={'email': 'test@test.com'})
	assert response.get_data() == b'Password reset link sent to email'


def test_set_profile_picture(client):
	response = client.post('/set_profile_picture', json={'email': 'test@test.com', 'profile_picture': 'profile.jpg'})
	assert response.get_data() == b'Profile picture set successfully'


def test_set_status_message(client):
	response = client.post('/set_status_message', json={'email': 'test@test.com', 'status_message': 'Hello, world!'})
	assert response.get_data() == b'Status message set successfully'


def test_block_contact(client):
	response = client.post('/block_contact', json={'email': 'test@test.com', 'contact_email': 'contact@test.com'})
	assert response.get_data() == b'Contact blocked successfully'


def test_unblock_contact(client):
	response = client.post('/unblock_contact', json={'email': 'test@test.com', 'contact_email': 'contact@test.com'})
	assert response.get_data() == b'Contact unblocked successfully'


def test_create_group(client):
	response = client.post('/create_group', json={'email': 'test@test.com', 'group_name': 'Test Group', 'group_picture': 'group.jpg'})
	assert response.get_data() == b'Group created successfully'


def test_edit_group(client):
	response = client.post('/edit_group', json={'email': 'test@test.com', 'group_name': 'Test Group', 'group_picture': 'group.jpg', 'new_group_name': 'New Test Group', 'new_group_picture': 'new_group.jpg'})
	assert response.get_data() == b'Group edited successfully'


def test_manage_group(client):
	response = client.post('/manage_group', json={'email': 'test@test.com', 'group_name': 'New Test Group', 'group_picture': 'new_group.jpg'})
	assert response.get_data() == b'Group managed'


def test_send_message(client):
	response = client.post('/send_message', json={'sender': 'test@test.com', 'receiver': 'receiver@test.com', 'content': 'Hello, world!', 'read_receipt': True, 'encryption': True, 'attachments': ['attachment.jpg']})
	assert 'message_id' in response.get_json()


def test_receive_message(client):
	response = client.get('/receive_message', json={'message_id': 1})
	assert 'sender' in response.get_json()


def test_post_status(client):
	response = client.post('/post_status', json={'email': 'test@test.com', 'content': 'Hello, world!', 'visibility': 'public', 'duration': 24})
	assert 'status_id' in response.get_json()


def test_view_status(client):
	response = client.get('/view_status', json={'status_id': 'test@test.com_20220101000000'})
	assert 'user' in response.get_json()

