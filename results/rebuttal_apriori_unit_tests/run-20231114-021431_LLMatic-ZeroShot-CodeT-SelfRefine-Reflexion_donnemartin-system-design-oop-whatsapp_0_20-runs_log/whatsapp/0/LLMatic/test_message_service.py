import pytest
from message_service import MessageService

@pytest.fixture

def message_service():
	return MessageService()

def test_send_receive_message(message_service):
	sender_id = 1
	receiver_id = 2
	message = 'Hello!'
	assert message_service.send_message(sender_id, receiver_id, message) == True
	assert message_service.receive_message(receiver_id) == (sender_id, message, False)

def test_mark_as_read(message_service):
	sender_id = 1
	receiver_id = 2
	message = 'Hello!'
	message_service.send_message(sender_id, receiver_id, message)
	assert message_service.mark_as_read(receiver_id, 0) == True

def test_encrypt_decrypt_message(message_service):
	sender_id = 1
	message = 'Hello!'
	encrypted_message = message_service.encrypt_message(sender_id, message)
	assert encrypted_message != message
	decrypted_message = message_service.decrypt_message(sender_id, encrypted_message)
	assert decrypted_message == message

def test_send_receive_image(message_service):
	sender_id = 1
	receiver_id = 2
	image_path = '/path/to/image.jpg'
	assert message_service.send_image(sender_id, receiver_id, image_path) == True
	assert message_service.receive_image(receiver_id) == (sender_id, image_path)

def test_send_receive_content(message_service):
	sender_id = 1
	receiver_id = 2
	content = 'Emoji 😀'
	assert message_service.send_content(sender_id, receiver_id, content) == True
	assert message_service.receive_content(receiver_id) == (sender_id, content)
