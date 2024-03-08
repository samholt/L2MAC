import pytest
from notification import Notification

def test_create_notification():
	notification = Notification('test_user', 'test_content')
	assert notification.recipient == 'test_user'
	assert notification.content == 'test_content'
	assert notification.status == 'unread'

def test_update_status():
	notification = Notification('test_user', 'test_content')
	notification.update_status('read')
	assert notification.status == 'read'

def test_send_email_alert():
	notification = Notification('test_user', 'test_content')
	notification.send_email_alert()
	# In a real system, we would check that the email was sent here. For this test, we just check that the method runs without errors.
