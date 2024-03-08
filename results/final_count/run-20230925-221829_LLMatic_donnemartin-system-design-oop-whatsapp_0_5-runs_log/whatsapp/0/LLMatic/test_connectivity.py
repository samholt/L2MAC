import messaging
import app


def test_queue_offline_message():
	message_id = messaging.queue_offline_message('user1', 'user2', 'Hello')
	assert message_id in messaging.offline_messages_db
	assert messaging.offline_messages_db[message_id]['message'] == 'Hello'


def test_send_offline_messages():
	messaging.queue_offline_message('user1', 'user2', 'Hello')
	messages = messaging.send_offline_messages('user2')
	assert len(messages) == 1
	assert messages[0][1]['message'] == 'Hello'


def test_user_status():
	status = app.user_status('user1')
	assert status == {'user_id': 'user1', 'status': 'online'}
	status = app.user_status('user3')
	assert status == {'user_id': 'user3', 'status': 'offline'}
