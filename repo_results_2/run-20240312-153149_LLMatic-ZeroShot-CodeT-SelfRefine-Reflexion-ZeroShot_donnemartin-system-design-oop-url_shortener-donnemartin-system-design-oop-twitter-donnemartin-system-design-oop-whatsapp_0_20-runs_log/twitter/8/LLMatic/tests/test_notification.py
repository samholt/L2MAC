import pytest
from user import User
from notification import Notification

def test_notification():
	user1 = User('user1', 'user1@test.com', 'testpassword')
	user2 = User('user2', 'user2@test.com', 'testpassword')
	user1.receive_notification('follow', user2)
	assert user1.notifications[0]['type'] == 'follow'
	assert user1.notifications[0]['triggered_by'] == 'user2'
	assert user1.notifications[0]['received_by'] == 'user1'
