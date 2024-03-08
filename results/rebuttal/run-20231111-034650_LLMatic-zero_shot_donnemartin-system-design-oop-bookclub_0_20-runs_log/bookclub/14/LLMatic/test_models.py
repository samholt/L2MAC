import pytest
from models.notification import Notification


def test_create_notification():
	notification = Notification(1, 'user1', 'Test message')
	assert notification.user == 'user1'
	assert notification.message == 'Test message'
	assert notification.read_status == False


def test_update_read_status():
	notification = Notification(1, 'user1', 'Test message')
	notification.update_read_status()
	assert notification.read_status == True
