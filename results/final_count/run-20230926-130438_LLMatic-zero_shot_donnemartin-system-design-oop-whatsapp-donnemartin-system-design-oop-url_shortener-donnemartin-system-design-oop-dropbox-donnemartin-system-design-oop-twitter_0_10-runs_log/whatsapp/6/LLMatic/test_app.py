import pytest
from app import app
from user import User
from message import Message

user = User()
message = Message()

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_queue_offline_message(client):
	response = client.post('/queue_offline_message', data={'sender_id': '1', 'receiver_id': '2', 'message_text': 'Hello'})
	assert response.data == b'Message queued for offline user'


def test_get_offline_messages(client):
	response = client.post('/get_offline_messages', data={'receiver_id': '2'})
	assert response.data == b'[["1","Hello"]]\n'


def test_set_online_status(client):
	response = client.post('/set_online_status', data={'user_id': '1', 'status': 'online'})
	assert response.data == b'Online status updated successfully'


def test_get_online_status(client):
	response = client.post('/get_online_status', data={'user_id': '1'})
	assert response.data == b'online'
