import messages


def test_send_message():
	messages.send_message('sender@test.com', 'recipient@test.com', 'Hello!')
	assert ('sender@test.com', 'recipient@test.com') in messages.messages_db


def test_queue_message():
	messages.send_message('sender@test.com', 'recipient@test.com', 'Hello!')
	messages.queue_message('sender@test.com', 'recipient@test.com')
	assert messages.messages_db[('sender@test.com', 'recipient@test.com')].queued


def test_read_message():
	messages.send_message('sender@test.com', 'recipient@test.com', 'Hello!')
	message = messages.read_message('sender@test.com', 'recipient@test.com')
	assert message.read_receipt


def test_update_read_receipt():
	messages.send_message('sender@test.com', 'recipient@test.com', 'Hello!')
	messages.update_read_receipt('sender@test.com', 'recipient@test.com')
	assert messages.messages_db[('sender@test.com', 'recipient@test.com')].read_receipt


def test_encrypt_message():
	messages.send_message('sender@test.com', 'recipient@test.com', 'Hello!')
	messages.encrypt_message('sender@test.com', 'recipient@test.com')
	assert messages.messages_db[('sender@test.com', 'recipient@test.com')].encrypted


def test_share_image():
	messages.share_image('sender@test.com', 'recipient@test.com', 'Image content')
	assert ('sender@test.com', 'recipient@test.com') in messages.messages_db
