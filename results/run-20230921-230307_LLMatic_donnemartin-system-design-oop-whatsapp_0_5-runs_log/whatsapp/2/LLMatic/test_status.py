import pytest
from status import Status
from user import User


def test_status():
	user = User('test@example.com', 'password')
	status = Status(user, 'Hello, world!', 'public')
	assert status.is_visible(user)
	assert not status.is_expired()
	status.post_status('Goodbye, world!')
	assert status.content == 'Goodbye, world!'
	status.set_visibility('private')
	assert not status.is_visible(User('other@example.com', 'password'))
