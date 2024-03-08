import pytest
import random
import string
from message_service import MessageService

message_service = MessageService()


def test_send_receive_messages():
	sender_id = random.randint(1, 100)
	receiver_id = random.randint(1, 100)
	message = f"Hello! {random.randint(1, 1000)}"
	assert message_service.send_message(sender_id, receiver_id, message) == True
	assert message_service.receive_message(receiver_id) == message


def test_end_to_end_encryption():
	sender_id = random.randint(1, 100)
	receiver_id = random.randint(1, 100)
	message = f"Secret {random.randint(1, 1000)}"
	encrypted_message = message_service.encrypt_message(sender_id, message)
	assert encrypted_message != message
	sent_message_id = message_service.send_message(sender_id, receiver_id, encrypted_message)
	received_encrypted_message = message_service.receive_message(receiver_id)
	decrypted_message = message_service.decrypt_message(receiver_id, received_encrypted_message)
	assert decrypted_message == message


def test_image_sharing():
	sender_id = random.randint(1, 100)
	receiver_id = random.randint(1, 100)
	image_path = f"/path/to/image{random.randint(1, 5)}.jpg"
	assert message_service.send_image(sender_id, receiver_id, image_path) == True
	assert message_service.receive_image(receiver_id) == image_path
