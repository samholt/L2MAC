import pytest
from offline_service import OfflineService


def test_set_offline():
	offline_service = OfflineService()
	assert offline_service.set_offline('user1') == True


def test_send_message():
	offline_service = OfflineService()
	offline_service.users['user1'] = 'offline'
	offline_service.users['user2'] = 'offline'
	assert offline_service.send_message('user1', 'user2', 'Hello') == 'Sent'


def test_set_online():
	offline_service = OfflineService()
	assert offline_service.set_online('user1') == True


def test_check_message_sent():
	offline_service = OfflineService()
	offline_service.users['user1'] = 'offline'
	offline_service.users['user2'] = 'offline'
	offline_service.send_message('user1', 'user2', 'Hello')
	assert offline_service.check_message_sent('user1', 'user2') == True
