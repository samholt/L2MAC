import pytest
import mock_db
from user import User


def test_post_status():
	db = mock_db.MockDB()
	user = User('test@test.com', 'password')
	db.add(user.email, user)
	user.post_status('image.jpg', 'public')
	assert len(user.statuses) == 1


def test_delete_status():
	db = mock_db.MockDB()
	user = User('test@test.com', 'password')
	db.add(user.email, user)
	user.post_status('image.jpg', 'public')
	user.delete_status(1)
	assert len(user.statuses) == 0


def test_get_status():
	db = mock_db.MockDB()
	user = User('test@test.com', 'password')
	db.add(user.email, user)
	user.post_status('image.jpg', 'public')
	status = user.get_status(1)
	assert status is not None
