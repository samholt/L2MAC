import pytest
from notification import Notification

def test_notification():
	user = 'test_user'
	event = 'test_event'
	notification = Notification(user, event)
	assert notification.user == user
	assert notification.event == event
	assert notification.send_notification() == f'Notification for {user}: {event}'
