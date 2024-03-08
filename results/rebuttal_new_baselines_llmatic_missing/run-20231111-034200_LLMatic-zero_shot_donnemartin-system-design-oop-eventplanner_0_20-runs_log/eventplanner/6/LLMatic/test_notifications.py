import notifications

def test_notification_creation():
	notification = notifications.Notification('email', 'Test message', '12:00')
	assert notification.type == 'email'
	assert notification.message == 'Test message'
	assert notification.time == '12:00'


def test_send_email_notification():
	notification = notifications.Notification('email', 'Test message', '12:00')
	notification.send_email_notification('test@example.com', 'Test message')


def test_send_sms_notification():
	notification = notifications.Notification('sms', 'Test message', '12:00')
	notification.send_sms_notification('1234567890', 'Test message')


def test_set_reminder():
	notification = notifications.Notification('reminder', 'Test message', '12:00')
	notification.set_reminder('12:00', 'Test message')
