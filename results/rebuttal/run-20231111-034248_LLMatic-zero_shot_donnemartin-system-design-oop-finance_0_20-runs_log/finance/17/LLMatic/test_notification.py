import pytest
from notification import Notification

def test_notification():
	notification = Notification()

	# Test adding and getting notifications
	notification.add_notification('user1', 'Test message')
	assert notification.get_notifications('user1') == ['Test message']

	# Test clearing notifications
	notification.clear_notifications('user1')
	assert notification.get_notifications('user1') == []

	# Test bill notification
	bill = {'name': 'Rent', 'due_date': '2022-12-01', 'amount': 1000}
	notification.send_bill_notification('user1', bill)
	assert 'Upcoming bill: Rent due on 2022-12-01. Amount: 1000' in notification.get_notifications('user1')

	# Test fraud alert
	transaction = {'description': 'Unusual purchase', 'date': '2022-12-01', 'amount': 500}
	notification.send_fraud_alert('user1', transaction)
	assert 'Unusual activity detected: Unusual purchase on 2022-12-01. Amount: 500' in notification.get_notifications('user1')
