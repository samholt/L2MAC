import pytest
from notifications import Notification

def test_notifications():
	user_notification = Notification('test_user')

	# Test bill notification
	user_notification.set_bill_notification('Electricity bill')
	assert 'Upcoming bill: Electricity bill' in user_notification.get_notifications()

	# Test payment notification
	user_notification.set_payment_notification('Rent payment')
	assert 'Upcoming payment: Rent payment' in user_notification.get_notifications()

	# Test unusual activity alert
	user_notification.alert_unusual_activity('Unusual login attempt')
	assert 'Alert! Unusual activity detected: Unusual login attempt' in user_notification.get_notifications()
