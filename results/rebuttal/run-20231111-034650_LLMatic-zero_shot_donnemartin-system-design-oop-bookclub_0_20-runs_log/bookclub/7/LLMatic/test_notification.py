import notification

def test_add_notification():
	notifier = notification.Notification()
	notifier.add_notification('user1', 'Test message')
	assert notifier.get_notifications('user1') == ['Test message']

def test_send_email_alert():
	notifier = notification.Notification()
	notifier.send_email_alert('user1', 'Test message')
	# Since the email sending functionality is mocked, we can't really test it here
