import pytest
from notification import Notification

def test_create_notification():
	user = 'test_user'
	content = 'test_content'
	notification = Notification(user, content)
	assert notification.create_notification() == {'user': user, 'content': content}

def test_send_notification(capsys):
	user = 'test_user'
	content = 'test_content'
	notification = Notification(user, content)
	notification.send_notification()
	captured = capsys.readouterr()
	assert captured.out == f'Notification sent to {user}: {content}\n'
