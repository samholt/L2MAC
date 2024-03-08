import pytest
from user import User
from status import Status


def test_status_creation():
	user = User('test@example.com', 'password')
	status = Status(user, 'image.jpg')
	assert status.user == user
	assert status.image == 'image.jpg'
	assert status.visibility == 'everyone'


def test_change_visibility():
	user = User('test@example.com', 'password')
	status = Status(user, 'image.jpg')
	status.change_visibility('only_me')
	assert status.visibility == 'only_me'
