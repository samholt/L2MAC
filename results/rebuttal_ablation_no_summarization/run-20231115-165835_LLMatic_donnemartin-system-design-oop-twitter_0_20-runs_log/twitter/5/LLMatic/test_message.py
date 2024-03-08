import message


def test_send_and_view_thread():
	m = message.Message()
	m.send('user1', 'user2', 'Hello')
	m.send('user2', 'user1', 'Hi')
	m.send('user1', 'user2', 'How are you?')
	thread = m.view_thread('user1', 'user2')
	assert len(thread) == 3
	assert thread[0]['text'] == 'Hello'
	assert thread[1]['text'] == 'Hi'
	assert thread[2]['text'] == 'How are you?'
