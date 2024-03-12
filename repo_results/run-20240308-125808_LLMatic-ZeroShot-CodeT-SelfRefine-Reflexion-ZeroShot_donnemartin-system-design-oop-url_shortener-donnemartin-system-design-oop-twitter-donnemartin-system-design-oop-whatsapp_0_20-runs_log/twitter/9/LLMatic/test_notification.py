import pytest
from user import User, register, authenticate
from notification import Notification


def test_notification():
	register('test2@test.com', 'testuser', 'password', False)
	user = authenticate('test2@test.com', 'password')
	user.receive_notification('like')
	assert len(user.notifications) == 1
	assert isinstance(user.notifications[0], Notification)
	assert user.notifications[0].user_id == 'test2@test.com'
	assert user.notifications[0].type == 'like'
