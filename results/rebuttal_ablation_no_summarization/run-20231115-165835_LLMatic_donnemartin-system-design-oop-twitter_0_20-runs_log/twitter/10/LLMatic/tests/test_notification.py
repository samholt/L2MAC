import pytest
from notification import Notification


def test_create_notification():
	user = 'test_user'
	content = 'test_content'
	notification = Notification(user, content)
	assert notification.create_notification() == {user: {'content': content}}
