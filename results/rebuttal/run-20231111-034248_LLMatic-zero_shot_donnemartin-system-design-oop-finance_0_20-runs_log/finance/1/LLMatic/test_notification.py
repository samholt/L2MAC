import pytest
from notification import Notification


def test_send_notification():
	notification = Notification()
	notification.send_notification('user1', 'You have exceeded your budget limit')
	assert notification.get_notifications('user1') == ['You have exceeded your budget limit']


def test_set_bill_alert():
	notification = Notification()
	notification.set_bill_alert('user1', '2022-12-01', 'Your electricity bill is due')
	assert notification.get_bill_alerts('user1') == [('2022-12-01', 'Your electricity bill is due')]


def test_set_fraud_alert():
	notification = Notification()
	notification.set_fraud_alert('user1', 'Unusual activity detected on your account')
	assert notification.get_fraud_alerts('user1') == ['Unusual activity detected on your account']
