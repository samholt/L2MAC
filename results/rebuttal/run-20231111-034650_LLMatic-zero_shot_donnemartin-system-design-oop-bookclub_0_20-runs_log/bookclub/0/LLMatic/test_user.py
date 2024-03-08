import pytest
from user import User


def test_user():
	user1 = User('User 1', 'user1@example.com', 'password1')
	user2 = User('User 2', 'user2@example.com', 'password2')

	# Test follow
	user1.follow(user2)
	assert user2 in user1.following

	# Test unfollow
	user1.unfollow(user2)
	assert user2 not in user1.following
