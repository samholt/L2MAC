import pytest
from notification import Notification

def test_set_and_get_notifications():
	notification = Notification()
	notification.set_notification('user1', 'Test notification')
	assert notification.get_notifications('user1') == ['Test notification']

def test_alert_unusual_activity():
	notification = Notification()
	notification.alert_unusual_activity('user1', 'Unusual activity detected')
	assert notification.get_notifications('user1') == ['Alert: Unusual activity detected']
