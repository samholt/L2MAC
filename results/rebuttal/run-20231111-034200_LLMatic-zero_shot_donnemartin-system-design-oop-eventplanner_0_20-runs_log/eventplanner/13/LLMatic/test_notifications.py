import pytest
from notifications import Notification

@pytest.fixture
def notification():
	return Notification()

def test_send_notification(notification):
	assert notification.send_notification('user1', 'Hello')
	assert notification.get_notifications('user1') == ['Hello']

def test_set_reminder(notification):
	assert notification.set_reminder('user1', 'Meeting at 10AM')
	assert notification.get_notifications('user1') == ['Meeting at 10AM']

def test_get_notifications(notification):
	assert notification.get_notifications('user1') == []
	assert notification.send_notification('user1', 'Hello')
	assert notification.get_notifications('user1') == ['Hello']
