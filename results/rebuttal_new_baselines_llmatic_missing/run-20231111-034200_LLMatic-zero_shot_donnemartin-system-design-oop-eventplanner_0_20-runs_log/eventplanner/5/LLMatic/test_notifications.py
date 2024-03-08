import pytest
from notifications import Notifications

def test_notifications():
	notifications = Notifications()

	# Test adding and getting notifications
	notifications.add_notification('user1', 'Test message 1')
	notifications.add_notification('user1', 'Test message 2')
	assert notifications.get_notifications('user1') == ['Test message 1', 'Test message 2']

	# Test clearing notifications
	notifications.clear_notifications('user1')
	assert notifications.get_notifications('user1') == []

	# Test sending email and SMS notifications
	notifications.send_email_notification('test@example.com', 'Test email message')
	notifications.send_sms_notification('1234567890', 'Test SMS message')
