import notifications

def test_import():
	assert notifications is not None

def test_send_notification():
	notification = notifications.Notification('User1', 'Test Notification')
	assert notification.send_notification() == 'Notification sent to User1: Test Notification'

def test_set_reminder():
	reminder = notifications.Notification('User1', 'Test Reminder')
	assert reminder.set_reminder('Test Reminder') == 'Reminder set for User1: Test Reminder'
