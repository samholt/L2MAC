import message


def test_send():
	msg = message.Message()
	message_id = msg.send('user1', 'user2', 'Hello!')
	assert message_id == 1
	assert msg.database[message_id] == {'sender': 'user1', 'receiver': 'user2', 'content': 'Hello!', 'timestamp': msg.database[message_id]['timestamp']}


def test_block():
	msg = message.Message()
	result = msg.block('user1', 'user2')
	assert result == True
	assert 'user2' in msg.database['user1']['blocked']
