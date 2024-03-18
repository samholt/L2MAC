import pytest
from notification import Notification
from user import User


def test_notification():
	user = User('test_user', 'test_password')
	notification = Notification(user, 'like')
	user.receive_notification(notification)

	assert len(user.notifications) == 1
	assert str(user.notifications[0]) == f'{user} received {notification.type} at {notification.timestamp}'
