import pytest
from message import MessageService

@pytest.fixture
def message_service():
	return MessageService()


def test_send_receive_messages(message_service):
	sender_id = 1
	receiver_id = 2
	message = 'Hello!'
	assert message_service.send_message(sender_id, receiver_id, message) == True
	assert message_service.receive_message(receiver_id) == (sender_id, message, False)


def test_read_receipts(message_service):
	sender_id = 1
	receiver_id = 2
	message = 'Test message'
	message_service.send_message(sender_id, receiver_id, message)
	assert message_service.mark_as_read(receiver_id, 0) == True


def test_end_to_end_encryption(message_service):
	sender_id = 1
	receiver_id = 2
	message = 'Secret'
	encrypted_message = message_service.encrypt_message(sender_id, message)
	assert encrypted_message != message
	sent_message_id = message_service.send_message(sender_id, receiver_id, encrypted_message)
	received_encrypted_message = message_service.receive_message(receiver_id)
	decrypted_message = message_service.decrypt_message(receiver_id, received_encrypted_message[1])
	assert decrypted_message == message


def test_image_sharing(message_service):
	sender_id = 1
	receiver_id = 2
	image_path = '/path/to/image.jpg'
	assert message_service.send_image(sender_id, receiver_id, image_path) == True
	assert message_service.receive_image(receiver_id) == (sender_id, image_path)


def test_emojis_gifs_stickers(message_service):
	sender_id = 1
	receiver_id = 2
	content = 'Emoji 😀'
	assert message_service.send_content(sender_id, receiver_id, content) == True
	assert message_service.receive_content(receiver_id) == (sender_id, content)
