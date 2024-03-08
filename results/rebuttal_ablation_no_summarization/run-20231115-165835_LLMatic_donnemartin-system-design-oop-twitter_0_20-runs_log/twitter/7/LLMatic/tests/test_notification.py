import pytest
import notification

def test_create_notification():
	new_notification = notification.create_notification('user1', 'You have a new follower')
	assert new_notification.user == 'user1'
	assert new_notification.text == 'You have a new follower'
	assert len(notification.notifications_db) == 1
