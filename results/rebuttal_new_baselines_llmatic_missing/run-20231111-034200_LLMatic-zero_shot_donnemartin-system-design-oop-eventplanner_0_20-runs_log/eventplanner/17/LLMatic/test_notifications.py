import pytest
from notifications import Notifications


def test_send_notification():
	notifications = Notifications()
	assert notifications.send_notification('user1', 'Test message') == 'Notification sent'
	assert notifications.get_notifications('user1') == ['Test message']


def test_set_reminder():
	notifications = Notifications()
	assert notifications.set_reminder('user1', 'Test reminder') == 'Reminder set'
	assert notifications.get_reminders('user1') == ['Test reminder']


def test_no_notifications():
	notifications = Notifications()
	assert notifications.get_notifications('user2') == 'No notifications'


def test_no_reminders():
	notifications = Notifications()
	assert notifications.get_reminders('user2') == 'No reminders'
