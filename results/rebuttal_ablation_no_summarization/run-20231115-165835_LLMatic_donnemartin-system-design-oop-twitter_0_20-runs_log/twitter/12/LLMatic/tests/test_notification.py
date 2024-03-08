import pytest
from notification import Notification, notifications_db


def test_create_notification():
	assert Notification.create_notification('user1', 'Notification text', 'Trigger')
	assert len(notifications_db['user1']) == 1
	assert notifications_db['user1'][0].text == 'Notification text'
	assert notifications_db['user1'][0].trigger == 'Trigger'

	assert Notification.create_notification('user2', 'Notification text', 'Trigger')
	assert len(notifications_db['user2']) == 1
	assert notifications_db['user2'][0].text == 'Notification text'
	assert notifications_db['user2'][0].trigger == 'Trigger'
