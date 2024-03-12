import message


def test_send_message():
	m = message.Message('user1', 'user2', 'Hello')
	assert m.send_message() == 'Message sent'


def test_block_user():
	m = message.Message('user1', 'user2', 'Hello')
	m.block_user('user1')
	assert m.send_message() == 'User is blocked'
