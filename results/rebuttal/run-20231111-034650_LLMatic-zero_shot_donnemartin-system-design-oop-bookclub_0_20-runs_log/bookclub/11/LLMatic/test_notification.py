import pytest
from notification import Notification

notification = Notification()

def test_send_notification():
	assert notification.send_notification('user1', 'Welcome to the book club!') == 'Notification sent to user1'

def test_send_email_alert():
	assert notification.send_email_alert('user1', 'Meeting reminder') == 'Email alert sent to user1'
