import datetime
from notifications import Notifications

def test_notifications():
	user = {'name': 'Test User'}
	notifications = Notifications(user)

	# Test setting a notification
	notifications.set_notification('Test notification')
	assert 'Test notification' in notifications.get_notifications()

	# Test setting an alert
	notifications.set_alert('Test alert')
	assert 'Test alert' in notifications.get_alerts()

	# Test checking for unusual activity
	transactions = [{} for _ in range(11)]
	notifications.check_for_unusual_activity(transactions)
	assert 'Unusual activity detected in your account' in notifications.get_alerts()

	# Test checking for upcoming bills
	bills = [{'name': 'Test Bill', 'due_date': datetime.datetime.now() + datetime.timedelta(days=6)}]
	notifications.check_for_upcoming_bills(bills)
	assert 'Your bill for Test Bill is due soon' in notifications.get_notifications()

