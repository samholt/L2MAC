import pytest
from user import User


def test_recommend_users():
	User.users.clear()
	user1 = User(1, 'test1@test.com', 'test1', 'password')
	user2 = User(2, 'test2@test.com', 'test2', 'password')
	user3 = User(3, 'test3@test.com', 'test3', 'password')
	user4 = User(4, 'test4@test.com', 'test4', 'password')
	user1.follow(2)
	user2.follow(3)
	user3.follow(4)
	recommended = user1.recommend_users()
	assert len(recommended) == 1
	assert recommended[0].id == 3
