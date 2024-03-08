import pytest
from offline_service import OfflineService

@pytest.fixture
def offline_service():
	return OfflineService()

def test_offline_online(offline_service):
	offline_service.set_offline(1)
	assert offline_service.user_status[1] == 'offline'
	offline_service.set_online(1)
	assert offline_service.user_status[1] == 'online'

def test_send_message(offline_service):
	offline_service.set_offline(1)
	assert offline_service.send_message(1, 2, 'Hello') == 'Queued'
	offline_service.set_online(1)
	assert offline_service.send_message(1, 2, 'Hello') == 'Sent'

def test_check_message_sent(offline_service):
	offline_service.set_offline(1)
	offline_service.send_message(1, 2, 'Hello')
	assert offline_service.check_message_sent(1, 2) == False
	offline_service.set_online(1)
	assert offline_service.check_message_sent(1, 2) == True
