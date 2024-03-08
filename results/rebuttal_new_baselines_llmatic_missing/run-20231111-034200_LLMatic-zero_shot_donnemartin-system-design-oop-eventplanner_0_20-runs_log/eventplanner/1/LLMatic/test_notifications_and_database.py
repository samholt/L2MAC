import pytest
from notifications import Notification
from database import Database

def test_notification():
	notification = Notification('Email', 'test@example.com', 'Test Content')
	assert notification.send_notification() == 'Sending Email notification to test@example.com with content: Test Content'
	assert notification.set_reminder('12:00') == 'Setting reminder for test@example.com at 12:00 with content: Test Content'

def test_database():
	db = Database()
	notification = Notification('Email', 'test@example.com', 'Test Content')
	db.add_notification('1', notification)
	assert db.get_notification('1') == notification
