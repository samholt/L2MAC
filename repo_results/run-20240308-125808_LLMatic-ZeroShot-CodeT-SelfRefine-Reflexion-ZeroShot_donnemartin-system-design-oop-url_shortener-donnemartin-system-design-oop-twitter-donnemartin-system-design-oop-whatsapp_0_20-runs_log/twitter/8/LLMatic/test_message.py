import message


def test_send_message():
	db = {}
	msg = message.Message('user1', 'user2', 'Hello!')
	assert msg.send(db) == 'Message sent'
	assert len(db['messages']) == 1
	assert db['messages'][0].text == 'Hello!'


def test_block_user():
	db = {}
	msg = message.Message('user1', 'user2', 'Hello!')
	msg.block('user1')
	assert msg.send(db) == 'User is blocked'
	assert 'messages' not in db
