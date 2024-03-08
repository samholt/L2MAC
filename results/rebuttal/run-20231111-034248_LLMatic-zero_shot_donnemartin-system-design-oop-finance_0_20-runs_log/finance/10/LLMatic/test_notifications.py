import pytest
from notifications import Notifications

def test_send_notification():
	notifications = Notifications()
	assert notifications.send_notification('user1', 'Test notification') == 'Notification sent'
	assert notifications.get_notifications('user1') == ['Test notification']

def test_alert_user():
	notifications = Notifications()
	assert notifications.alert_user('user1', 'Test alert') == 'Alert sent'
	assert notifications.get_notifications('user1') == ['Test alert']

def test_get_notifications():
	notifications = Notifications()
	notifications.send_notification('user1', 'Test notification')
	notifications.alert_user('user1', 'Test alert')
	assert notifications.get_notifications('user1') == ['Test notification', 'Test alert']
