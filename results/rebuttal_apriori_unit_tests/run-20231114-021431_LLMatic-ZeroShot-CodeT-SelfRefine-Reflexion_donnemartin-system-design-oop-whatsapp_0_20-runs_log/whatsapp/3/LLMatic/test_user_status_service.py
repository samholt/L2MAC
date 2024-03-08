import pytest
from user_status_service import UserStatusService


def test_set_status():
	user_status_service = UserStatusService()
	assert user_status_service.set_status('user1', 'online') == True


def test_get_status():
	user_status_service = UserStatusService()
	user_status_service.set_status('user1', 'online')
	assert user_status_service.get_status('user1') == 'online'
