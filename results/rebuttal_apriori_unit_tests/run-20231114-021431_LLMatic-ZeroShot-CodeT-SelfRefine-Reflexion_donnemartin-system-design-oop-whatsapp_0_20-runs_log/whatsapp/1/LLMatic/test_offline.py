import pytest
from offline import OfflineService

@pytest.fixture
def offline_service():
	return OfflineService()

def test_set_offline(offline_service):
	user_id = 1
	offline_service.set_offline(user_id)
	assert offline_service.user_status[user_id] == 'offline'

def test_set_online(offline_service):
	user_id = 1
	offline_service.set_online(user_id)
	assert offline_service.user_status[user_id] == 'online'

def test_send_message(offline_service):
	sender_id = 1
	receiver_id = 2
	message = 'Hello'
	offline_service.set_offline(sender_id)
	assert offline_service.send_message(sender_id, receiver_id, message) == 'Queued'
	offline_service.set_online(sender_id)
	assert offline_service.send_message(sender_id, receiver_id, message) == 'Sent'

def test_check_message_sent(offline_service):
	sender_id = 1
	receiver_id = 2
	message = 'Hello'
	offline_service.set_offline(sender_id)
	offline_service.send_message(sender_id, receiver_id, message)
	assert offline_service.check_message_sent(sender_id, receiver_id) == False
	offline_service.set_online(sender_id)
	assert offline_service.check_message_sent(sender_id, receiver_id) == True
