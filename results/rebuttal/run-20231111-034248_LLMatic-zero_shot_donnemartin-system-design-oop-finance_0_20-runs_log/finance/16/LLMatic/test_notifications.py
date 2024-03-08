import pytest
from notifications import Notifications


def test_add_notification():
	user = 'Test User'
	notifications = Notifications(user)
	message = 'Test Notification'
	assert notifications.add_notification(message) == [message]


def test_alert_unusual_activity():
	user = 'Test User'
	notifications = Notifications(user)
	transaction = 'Test Transaction'
	notifications.alert_unusual_activity(transaction)
	assert notifications.notifications[0] == f'Unusual activity detected: {transaction}'


def test_notify_upcoming_payment():
	user = 'Test User'
	notifications = Notifications(user)
	bill = 'Test Bill'
	notifications.notify_upcoming_payment(bill)
	assert notifications.notifications[0] == f'Upcoming payment due: {bill}'
