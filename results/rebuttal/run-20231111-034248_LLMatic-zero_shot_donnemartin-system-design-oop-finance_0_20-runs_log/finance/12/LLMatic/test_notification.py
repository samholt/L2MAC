import pytest
from notification import Notification

def test_set_notification():
	notification = Notification()
	assert notification.set_notification('user1', 'Bill due in 3 days') == 'Notification set successfully'
	assert notification.get_notifications('user1') == ['Bill due in 3 days']

def test_alert_unusual_activity():
	notification = Notification()
	assert notification.alert_unusual_activity('user1', 'Unusual activity detected') == 'Alert set successfully'
	assert notification.get_notifications('user1') == ['Unusual activity detected']
