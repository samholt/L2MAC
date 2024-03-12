import message


def test_send_message():
	m = message.Message()
	assert m.send('user1', 'user2', 'Hello') == 'Message sent'
	assert m.send('user1', 'user2', 'Hello again') == 'Message sent'
	assert len(m.messages['user2']) == 2


def test_block_user():
	m = message.Message()
	assert m.block_user('user2', 'user1') == 'User blocked'
	assert m.send('user1', 'user2', 'Hello') == 'User is blocked'


def test_unblock_user():
	m = message.Message()
	m.block_user('user2', 'user1')
	assert m.unblock_user('user2', 'user1') == 'User unblocked'
	assert m.send('user1', 'user2', 'Hello') == 'Message sent'
