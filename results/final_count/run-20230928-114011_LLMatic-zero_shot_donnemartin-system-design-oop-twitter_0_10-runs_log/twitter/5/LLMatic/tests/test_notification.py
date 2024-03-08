import pytest
from notification import Notification

def test_create_notification():
	assert Notification.create_notification(1, 'Test content', 'Test recipient', 'Test related') == 'Notification created'
	assert Notification.create_notification(1, 'Test content', 'Test recipient', 'Test related') == 'Notification already exists'

def test_delete_notification():
	assert Notification.delete_notification(1) == 'Notification deleted'
	assert Notification.delete_notification(1) == 'Notification does not exist'

def test_notify_users():
	assert Notification.notify_users(2, 'Test content', 'Test recipient', 'Test related') == 'User notified'
	assert Notification.create_notification(2, 'Test content', 'Test recipient', 'Test related') == 'Notification already exists'
