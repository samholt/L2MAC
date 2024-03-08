import messaging


def test_send_message():
	message_id = messaging.send_message('user1', 'user2', 'Hello')
	assert message_id in messaging.messages_db
	assert messaging.messages_db[message_id]['message'] == 'Hello'


def test_receive_messages():
	messaging.send_message('user1', 'user2', 'Hello')
	messaging.send_message('user2', 'user1', 'Hi')
	messages = messaging.receive_messages('user1')
	assert len(messages) == 1
	assert messages[0]['message'] == 'Hi'


def test_handle_read_receipt():
	message_id = messaging.send_message('user1', 'user2', 'Hello')
	assert not messaging.messages_db[message_id]['read']
	messaging.handle_read_receipt(message_id)
	assert messaging.messages_db[message_id]['read']


def test_encrypt_message():
	encrypted_message = messaging.encrypt_message('Hello')
	assert encrypted_message == messaging.encrypt_message('Hello')


def test_share_media():
	media_id = messaging.share_media('user1', 'user2', 'emoji')
	assert media_id in messaging.media_db
	assert messaging.media_db[media_id]['media'] == 'emoji'
