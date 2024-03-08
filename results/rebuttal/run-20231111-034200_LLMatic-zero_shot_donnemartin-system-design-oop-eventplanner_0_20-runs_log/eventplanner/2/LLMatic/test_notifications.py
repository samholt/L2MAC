import pytest
from notifications import Notifications

def test_add_notification():
	notifications = Notifications()
	assert notifications.add_notification('user1', 'Notification 1') == True
	assert notifications.get_notifications('user1') == ['Notification 1']


def test_clear_notifications():
	notifications = Notifications()
	notifications.add_notification('user1', 'Notification 1')
	assert notifications.clear_notifications('user1') == True
	assert notifications.get_notifications('user1') == []
