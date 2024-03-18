from chat import Chat, Message

def test_chat_creation():
	chat = Chat('Test Chat')
	assert chat.name == 'Test Chat'
	assert chat.messages == []

	chat_dict = chat.to_dict()
	assert 'id' in chat_dict
	assert chat_dict['name'] == 'Test Chat'
	assert chat_dict['messages'] == []

def test_message_creation():
	message = Message('user_id', 'Hello, World!')
	assert message.user_id == 'user_id'
	assert message.content == 'Hello, World!'

	message_dict = message.to_dict()
	assert 'id' in message_dict
	assert message_dict['user_id'] == 'user_id'
	assert message_dict['content'] == 'Hello, World!'

def test_send_message():
	chat = Chat('Test Chat')
	message = chat.send_message('user_id', 'Hello, World!')
	assert message in chat.messages
