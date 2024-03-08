import messaging

def test_send_message():
	messaging_service = messaging.Messaging()
	messaging_service.send_message('sender@test.com', 'receiver@test.com', 'Hello!')
	messages = messaging_service.get_messages('receiver@test.com')
	assert len(messages) == 1
	assert messages[0]['sender'] == 'sender@test.com'
	assert messages[0]['message'] == 'Hello!'
	assert messages[0]['status'] == 'unread'

def test_read_message():
	messaging_service = messaging.Messaging()
	messaging_service.send_message('sender@test.com', 'receiver@test.com', 'Hello!')
	messaging_service.read_message('sender@test.com', 'receiver@test.com', 0)
	messages = messaging_service.get_messages('receiver@test.com')
	assert messages[0]['status'] == 'read'
	receipts = messaging_service.get_receipts('sender@test.com')
	assert receipts['receiver'] == 'receiver@test.com'
	assert receipts['message_id'] == 0
	assert receipts['status'] == 'read'

def test_create_group_chat():
	messaging_service = messaging.Messaging()
	messaging_service.create_group_chat('creator@test.com', 'Test Group', 'group_picture.jpg', ['participant1@test.com', 'participant2@test.com'])
	group_chat = messaging_service.group_chats['Test Group']
	assert group_chat['creator'] == 'creator@test.com'
	assert group_chat['picture'] == 'group_picture.jpg'
	assert 'participant1@test.com' in group_chat['participants']
	assert 'participant2@test.com' in group_chat['participants']

def test_update_participants():
	messaging_service = messaging.Messaging()
	messaging_service.create_group_chat('creator@test.com', 'Test Group', 'group_picture.jpg', ['participant1@test.com', 'participant2@test.com'])
	messaging_service.update_participants('creator@test.com', 'Test Group', ['participant3@test.com', 'participant4@test.com'])
	group_chat = messaging_service.group_chats['Test Group']
	assert 'participant3@test.com' in group_chat['participants']
	assert 'participant4@test.com' in group_chat['participants']

def test_online_status():
	messaging_service = messaging.Messaging()
	messaging_service.set_online_status('user@test.com', 'online')
	assert messaging_service.get_online_status('user@test.com') == 'online'
	messaging_service.set_online_status('user@test.com', 'offline')
	assert messaging_service.get_online_status('user@test.com') == 'offline'
