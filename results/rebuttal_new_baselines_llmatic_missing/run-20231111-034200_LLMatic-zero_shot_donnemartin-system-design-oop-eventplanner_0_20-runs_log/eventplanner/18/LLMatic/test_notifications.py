from notifications import Notification

def test_notification():
	# Create a notification
	notification = Notification('email', 'Test content')

	# Test sending email
	notification.send_email('test@example.com')

	# Test sending sms
	notification.send_sms('1234567890')

	# Test setting reminder
	notification.set_reminder('2022-12-31 23:59:59')
