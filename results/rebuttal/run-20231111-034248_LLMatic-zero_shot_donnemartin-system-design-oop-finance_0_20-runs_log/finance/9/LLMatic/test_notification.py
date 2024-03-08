import pytest
from notification import Notification, NotificationManager
from user import User


def test_notification():
	user = User('John Doe', 'password', 'john.doe@example.com')
	message = 'Unusual account activity detected.'
	notification = Notification(user, message)
	assert notification.user == user
	assert notification.message == message
	assert 'Alert for John Doe: Unusual account activity detected.' in notification.alert_user()


def test_notification_manager():
	manager = NotificationManager()
	user = User('John Doe', 'password', 'john.doe@example.com')
	message = 'Unusual account activity detected.'
	alert_message = manager.create_notification(user, message)
	assert 'Alert for John Doe: Unusual account activity detected.' in alert_message
	assert user.username in manager.notifications
	assert manager.notifications[user.username].message == message

