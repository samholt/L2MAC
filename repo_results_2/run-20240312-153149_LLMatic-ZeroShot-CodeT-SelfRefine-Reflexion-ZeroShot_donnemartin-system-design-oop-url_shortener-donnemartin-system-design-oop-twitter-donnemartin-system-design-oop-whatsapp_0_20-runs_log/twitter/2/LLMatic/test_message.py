import message


def test_send_message():
	m = message.Message()
	assert m.send('user1', 'user2', 'Hello') == 'Message sent'
	assert len(m.database) == 1


def test_block_user():
	m = message.Message()
	m.block('user1', 'user2')
	assert 'user2' in m.blocked['user1']
	assert m.send('user1', 'user2', 'Hello') == 'User is blocked'
