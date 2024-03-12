import pytest
from notification import Notification

def test_create_notification():
	notification = Notification(None, None, None, None)
	notification.create_notification(1, 1, 'like')
	assert notification.id == 1
	assert notification.user_id == 1
	assert notification.post_id == 1
	assert notification.type == 'like'


def test_view_notifications():
	Notification.clear_notifications()
	notification1 = Notification(None, None, None, None)
	notification1.create_notification(1, 1, 'like')
	notification2 = Notification(None, None, None, None)
	notification2.create_notification(2, 2, 'retweet')
	assert len(Notification.view_notifications(1)) == 1
	assert len(Notification.view_notifications(2)) == 1
