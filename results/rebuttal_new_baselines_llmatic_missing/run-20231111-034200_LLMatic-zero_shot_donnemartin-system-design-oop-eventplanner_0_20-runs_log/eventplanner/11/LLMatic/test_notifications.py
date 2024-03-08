import pytest
from notifications import Notifications

def test_notifications():
	notifications = Notifications()

	# Test adding a notification
	notifications.add_notification('user1', 'event1', 'Notification 1')
	assert notifications.get_notifications('user1') == {'event1': 'Notification 1'}

	# Test getting notifications
	notifications.add_notification('user1', 'event2', 'Notification 2')
	assert notifications.get_notifications('user1') == {'event1': 'Notification 1', 'event2': 'Notification 2'}

	# Test removing a notification
	notifications.remove_notification('user1', 'event1')
	assert notifications.get_notifications('user1') == {'event2': 'Notification 2'}
