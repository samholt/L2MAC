import pytest
from user import User, register, authenticate, mock_db


def test_register():
	assert register('test1@test.com', 'testuser1', 'testpass', False) == True
	assert register('test2@test.com', 'testuser2', 'testpass', False) == True


def test_authenticate():
	assert authenticate('testuser1', 'testpass') == True
	assert authenticate('testuser2', 'testpass') == True


def test_view_notifications():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	user1.follow(user2)
	assert user2.view_notifications() == ['testuser1 started following you.']


def test_recommend_users():
	user1 = User('test1@test.com', 'testuser1', 'testpass', False)
	user2 = User('test2@test.com', 'testuser2', 'testpass', False)
	user3 = User('test3@test.com', 'testuser3', 'testpass', False)
	mock_db['testuser1'] = user1
	mock_db['testuser2'] = user2
	mock_db['testuser3'] = user3
	user1.follow(user2)
	user3.follow(user2)
	user2.follow(user1)
	user2.follow(user3)
	assert set(user1.recommend_users()) == set(['testuser3'])

