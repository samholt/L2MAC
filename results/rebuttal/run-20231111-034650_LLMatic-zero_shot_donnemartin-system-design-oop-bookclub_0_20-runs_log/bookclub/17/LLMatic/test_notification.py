import pytest
from notification import Notification
from database import Database

def test_notification():
	db = Database()
	notification = Notification(db)

	# Test creating a notification
	notification.create_notification('1', {'message': 'Test message'})
	assert notification.get_notification('1') == {'message': 'Test message'}

	# Test updating a notification
	notification.update_notification('1', {'message': 'Updated message'})
	assert notification.get_notification('1') == {'message': 'Updated message'}

	# Test deleting a notification
	notification.delete_notification('1')
	assert notification.get_notification('1') is None
