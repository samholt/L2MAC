from message import Message

def test_message():
	message = Message('sender', 'receiver', 'Hello, World!', encryption=True)
	assert message.content == 'Hello, World!'
	message.encrypt()
	assert message.content != 'Hello, World!'
	message.decrypt()
	assert message.content == 'Hello, World!'

	message.attach('image.jpg')
	assert 'image.jpg' in message.attachments

	mock_db = {}
	message_id = message.send(mock_db)
	assert mock_db[message_id] == message

	received_message = Message.receive(mock_db, message_id)
	assert received_message == message
