import pytest
from notifications import Notifications

def test_send_notification():
	notifications = Notifications()
	assert notifications.send_notification('user1', 'Event milestone reached') == 'Notification sent'
	assert 'Event milestone reached' in notifications.notifications_db['user1']

def test_set_reminder():
	notifications = Notifications()
	assert notifications.set_reminder('user1', 'Task deadline approaching') == 'Reminder set'
	assert 'Task deadline approaching' in notifications.notifications_db['user1']
