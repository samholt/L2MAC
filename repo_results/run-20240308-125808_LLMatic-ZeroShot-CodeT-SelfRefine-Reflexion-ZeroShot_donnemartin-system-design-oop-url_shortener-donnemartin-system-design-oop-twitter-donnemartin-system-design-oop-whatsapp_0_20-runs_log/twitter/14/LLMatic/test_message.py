import message


def test_message():
	m = message.Message('sender', 'receiver', 'Hello!')
	assert m.sender == 'sender'
	assert m.receiver == 'receiver'
	assert m.text == 'Hello!'

	# Test sending a message
	db = {}
	assert m.send(db) == 'Message sent'
	assert db[m.id] == m

	# Test blocking a user
	m.block_user('receiver')
	assert 'receiver' in m.blocked_users

	# Test unblocking a user
	m.unblock_user('receiver')
	assert 'receiver' not in m.blocked_users
