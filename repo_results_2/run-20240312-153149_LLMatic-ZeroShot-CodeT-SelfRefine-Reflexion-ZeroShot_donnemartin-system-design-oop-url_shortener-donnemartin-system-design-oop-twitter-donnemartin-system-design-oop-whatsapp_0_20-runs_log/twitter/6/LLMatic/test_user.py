import pytest
from user import User


def test_receive_notification():
	user = User('test@test.com', 'testuser', 'testpassword', False)
	user.receive_notification('Test notification')
	assert user.notifications[0] == 'Test notification'


def test_get_recommendations():
	user1 = User('test1@test.com', 'testuser1', 'testpassword1', False)
	user2 = User('test2@test.com', 'testuser2', 'testpassword2', False)
	user3 = User('test3@test.com', 'testuser3', 'testpassword3', False)
	db = {user1.email: user1, user2.email: user2, user3.email: user3}
	user1.follow(user2)
	recommendations = user1.get_recommendations(db)
	assert len(recommendations) == 1
	assert recommendations[0] == user3.email
