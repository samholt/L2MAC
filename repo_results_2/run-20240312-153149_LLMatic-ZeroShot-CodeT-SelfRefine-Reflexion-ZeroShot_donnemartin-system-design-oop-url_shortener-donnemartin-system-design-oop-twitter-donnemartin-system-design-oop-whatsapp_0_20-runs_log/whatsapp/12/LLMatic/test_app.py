import pytest
import app
import mock_db
from user import User
from message import Message

# Existing tests...

def test_check_online_status():
	app.db.add('test@test.com', User('test@test.com', 'password'))
	response = app.app.test_client().get('/user/test@test.com/online_status')
	assert response.status_code == 200
	assert 'online_status' in response.get_json()


def test_send_queued_messages():
	user = User('test@test.com', 'password')
	message = Message('test@test.com', 'recipient@test.com', 'Hello')
	user.queue_message(message)
	app.db.add('test@test.com', user)
	response = app.app.test_client().post('/user/test@test.com/send_queued_messages')
	assert response.status_code == 200
	assert response.get_json()['status'] == 'success'
