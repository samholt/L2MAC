import pytest
from notifications import Notifications

def test_notifications():
	notifications = Notifications()

	user_id = 'user1'
	activity = 'Large withdrawal'
	payment = 'Rent'

	notifications.alert_unusual_activity(user_id, activity)
	notifications.alert_upcoming_payment(user_id, payment)

	assert len(notifications.get_notifications(user_id)) == 2
	assert 'Unusual activity detected: Large withdrawal' in notifications.get_notifications(user_id)
	assert 'Upcoming payment due: Rent' in notifications.get_notifications(user_id)
