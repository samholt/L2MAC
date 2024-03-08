import pytest
from status import Status
from user import User


def test_post_status():
	user = User()
	user.register('test@example.com', 'password')
	status = Status()
	status.post_status(user, 'image.jpg', 'public')
	assert status.user == user
	assert status.image == 'image.jpg'
	assert status.visibility == 'public'


def test_is_visible():
	user = User()
	user.register('test@example.com', 'password')
	status = Status()
	status.post_status(user, 'image.jpg', 'public')
	assert status.is_visible() is True

