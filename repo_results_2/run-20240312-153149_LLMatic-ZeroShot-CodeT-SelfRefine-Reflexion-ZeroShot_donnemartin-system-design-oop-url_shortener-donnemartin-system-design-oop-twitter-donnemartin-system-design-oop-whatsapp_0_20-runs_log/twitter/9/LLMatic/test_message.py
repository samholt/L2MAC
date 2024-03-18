import message


def test_send_message():
	msg = message.Message()
	assert msg.send_message('user1', 'user2', 'Hello') == 'Message sent'
	assert msg.send_message('user2', 'user1', 'Hi') == 'Message sent'
	assert len(msg.messages['user2']) == 1
	assert len(msg.messages['user1']) == 1


def test_block_user():
	msg = message.Message()
	assert msg.block_user('user1', 'user2') == 'User blocked'
	assert msg.send_message('user2', 'user1', 'Hi') == 'User is blocked'
