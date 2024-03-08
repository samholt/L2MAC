import pytest
from messaging import Messaging


def test_send_receive_message():
	messaging = Messaging()
	messaging.send_message('Hello', 'Bob')
	messaging.receive_message('Hello', 'Alice')
	assert 'Hello' in messaging.messages['Bob']
	assert 'Hello' in messaging.messages['Alice']


def test_display_read_receipt():
	messaging = Messaging()
	messaging.receive_message('Hello', 'Alice')
	assert messaging.display_read_receipt('Hello') == 'Message has been read'


def test_encrypt_decrypt_message():
	messaging = Messaging()
	encrypted_message = messaging.encrypt_message('Hello')
	decrypted_message = messaging.decrypt_message(encrypted_message)
	assert decrypted_message == 'Hello'


def test_share_image():
	messaging = Messaging()
	messaging.share_image('image_file', 'Bob')
	assert 'image_file' in messaging.messages['Bob']
