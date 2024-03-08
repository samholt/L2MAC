import pytest
from message import Message
from user import Auth

auth = Auth()

auth.sign_up('sender@test.com', 'password')
auth.sign_up('receiver@test.com', 'password')

def test_send_receive_message():
	message = Message('sender@test.com', 'receiver@test.com', 'Hello, World!')
	auth.users['receiver@test.com'].set_online_status(False)
	sent_message = message.send_message()
	assert sent_message == {'sender': 'sender@test.com', 'receiver': 'receiver@test.com', 'message': 'Message queued'}

	auth.users['receiver@test.com'].set_online_status(True)
	sent_message = message.send_message()
	assert sent_message == {'sender': 'sender@test.com', 'receiver': 'receiver@test.com', 'message': message.encrypted_content}

	received_message = auth.users['receiver@test.com'].receive_message(sent_message['message'])
	assert received_message == sent_message['message']
	assert message.read_receipt == True

def test_queued_messages():
	message1 = Message('sender@test.com', 'receiver@test.com', 'Hello, World!')
	message2 = Message('sender@test.com', 'receiver@test.com', 'Hello again, World!')
	auth.users['receiver@test.com'].set_online_status(False)
	message1.send_message()
	message2.send_message()
	assert len(auth.users['receiver@test.com'].queued_messages) == 2

	auth.users['receiver@test.com'].set_online_status(True)
	message1.send_queued_messages()
	assert len(auth.users['receiver@test.com'].queued_messages) == 0
