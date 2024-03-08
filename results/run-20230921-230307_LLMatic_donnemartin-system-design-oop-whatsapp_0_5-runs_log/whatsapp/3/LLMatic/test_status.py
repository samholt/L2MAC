import pytest
from status import Status
from user import User

def test_post():
	user = User('test@example.com', 'password')
	status = Status(user, 'image.jpg', 'public')
	status.post()
	assert status in user.statuses

def test_view():
	user1 = User('test1@example.com', 'password')
	user2 = User('test2@example.com', 'password')
	user1.contacts.append(user2)
	status = Status(user2, 'image.jpg', 'public')
	status.post()
	assert status in status.view(user1)

def test_manage():
	user = User('test@example.com', 'password')
	status = Status(user, 'image.jpg', 'public')
	status.post()
	status.manage()
	assert status not in user.statuses
