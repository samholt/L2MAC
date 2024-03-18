import pytest
from notification import Notification
from user import User

def test_create_notification():
	user = User(1, 'test@test.com', 'test', 'password')
	notification = Notification(user, 'test')
	notification.create_notification()
	assert len(user.notifications) == 1

def test_view_notifications():
	user = User(1, 'test@test.com', 'test', 'password')
	notification = Notification(user, 'test')
	notification.create_notification()
	notifications = notification.view_notifications()
	assert len(notifications) == 1
	assert notifications[0]['notification_type'] == 'test'
