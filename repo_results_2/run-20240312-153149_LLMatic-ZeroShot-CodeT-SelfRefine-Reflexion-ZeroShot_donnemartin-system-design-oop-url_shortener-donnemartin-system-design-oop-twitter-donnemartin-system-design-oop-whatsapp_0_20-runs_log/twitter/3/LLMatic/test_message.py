import message


def test_send_message():
	m = message.Message()
	assert m.send_message('user1', 'user2', 'Hello') == 'Message sent'
	assert m.send_message('user2', 'user1', 'Hi') == 'Message sent'
	assert len(m.messages['user1']) == 1
	assert len(m.messages['user2']) == 1


def test_block_user():
	m = message.Message()
	assert m.block_user('user1', 'user2') == 'User blocked'
	assert m.send_message('user2', 'user1', 'Hi') == 'User is blocked'


def test_unblock_user():
	m = message.Message()
	m.block_user('user1', 'user2')
	assert m.unblock_user('user1', 'user2') == 'User unblocked'
	assert m.send_message('user2', 'user1', 'Hi') == 'Message sent'
