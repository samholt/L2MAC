import pytest
from services.message_service import MessageService

def test_message_service():
	message_service = MessageService()

	# Test sending a message
	message = message_service.send_message(1, 2, 'Hello, World!')
	assert message['sender'] == 1
	assert message['receiver'] == 2
	assert message['message'] == 'Hello, World!'
	assert message['read_receipt'] == 0
	assert message['encrypted'] == 0

	# Test queuing a message
	# TODO: Implement these tests once the methods are implemented
	# queue_message('receiver@test.com', 'Hello, World!')

	# Test sending queued messages
	# send_queued_messages()
