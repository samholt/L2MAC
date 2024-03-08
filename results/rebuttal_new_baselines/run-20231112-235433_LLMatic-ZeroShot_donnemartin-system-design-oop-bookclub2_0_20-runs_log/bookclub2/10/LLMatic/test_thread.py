import pytest
from thread import Thread
from user import User


def test_thread_creation():
	user = User('1', 'John Doe', 'johndoe@example.com', 'password')
	thread = Thread('1', 'Test Thread', user)
	assert thread.id == '1'
	assert thread.title == 'Test Thread'
	assert thread.creator == user
	assert thread.comments == []


def test_add_comment():
	user = User('1', 'John Doe', 'johndoe@example.com', 'password')
	thread = Thread('1', 'Test Thread', user)
	thread.add_comment('This is a test comment.')
	assert thread.comments == ['This is a test comment.']
