import pytest
import notifications

def test_send_notification():
	notification = notifications.Notification('email', 'Test email')
	assert notifications.send_notification(notification) == 'Notification sent'

def test_get_notifications():
	notification = notifications.Notification('email', 'Test email')
	notifications.send_notification(notification)
	assert notifications.get_notifications('email') == 'Test email'

def test_set_reminder():
	assert notifications.set_reminder('reminder', 'Test reminder') == 'Reminder set'
