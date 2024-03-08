import pytest
import notifications

def test_import():
	assert notifications is not None

def test_notification():
	# Create a notification
	notification = notifications.Notification('Test', 'This is a test notification')
	# Test sending email
	notification.send_email('test@example.com')
	# Test sending sms
	notification.send_sms('1234567890')
	# Test setting reminder
	notification.set_reminder('2022-12-31 23:59:59')
