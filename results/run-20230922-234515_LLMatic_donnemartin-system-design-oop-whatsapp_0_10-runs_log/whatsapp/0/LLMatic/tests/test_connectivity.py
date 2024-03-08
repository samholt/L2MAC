import pytest
from utils import connectivity

def test_is_connected():
	# This test assumes that the machine running the tests has internet connectivity.
	assert connectivity.is_connected() is True

def test_queue_message():
	user_id = 1
	message = "Hello, World!"
	connectivity.queue_message(user_id, message)
	assert message in connectivity.message_queue[user_id]

def test_send_queued_messages():
	user_id = 1
	message = "Hello, World!"
	connectivity.queue_message(user_id, message)
	messages = connectivity.send_queued_messages(user_id)
	assert message in messages
	assert user_id not in connectivity.message_queue
