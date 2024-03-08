import pytest
from notifications import Notification

def test_send_notification():
	notification = Notification('email', 'Test notification')
	assert notification.send_notification('user1', 'Test notification') == 'Notification sent'

def test_set_reminder():
	notification = Notification('reminder', 'Test reminder')
	assert notification.set_reminder('user1', 'Test reminder') == 'Reminder set'
